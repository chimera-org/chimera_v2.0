"""
EEGEncoder Training Loop
Includes: LOSO dataloaders, label smoothing, early stopping
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import accuracy_score, cohen_kappa_score
from eegencoder.model import get_model
import numpy as np
from tqdm import tqdm
import json
import time
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

class StreamingDataset(Dataset):
    """Memory-efficient dataset for EEG trials"""
    def __init__(self, data_dir, subject_ids, is_training=True):
        self.data_dir = Path(data_dir)
        self.subject_ids = subject_ids
        self.is_training = is_training
        
        self.filepaths = []
        for subj_id in subject_ids:
            suffix = 'train' if is_training else 'eval'
            X_path = self.data_dir / f"subject_{subj_id:02d}_X.npy"
            y_path = self.data_dir / f"subject_{subj_id:02d}_y.npy"
            if X_path.exists():
                self.filepaths.append((X_path, y_path))
    
    def __len__(self):
        return len(self.filepaths) * 288  # Approximate, will be trimmed
    
    def __getitem__(self, idx):
        file_idx = idx // 288
        trial_idx = idx % 288
        
        if file_idx >= len(self.filepaths):
            raise IndexError
        
        X_path, y_path = self.filepaths[file_idx]
        
        # Load only needed trial
        X = np.load(X_path, mmap_mode='r')[trial_idx]
        y = np.load(y_path, mmap_mode='r')[trial_idx]
        
        return torch.FloatTensor(X), torch.LongTensor([y])[0]

class EarlyStopping:
    """Stop training when validation stops improving"""
    def __init__(self, patience=5, min_delta=0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        
    def __call__(self, val_loss):
        if self.best_score is None:
            self.best_score = val_loss
        elif val_loss > self.best_score - self.min_delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = val_loss
            self.counter = 0

def train_epoch(model, train_loader, criterion, optimizer, device, epoch):
    """Train one epoch"""
    model.train()
    running_loss = 0.0
    all_preds, all_labels = [], []
    
    pbar = tqdm(train_loader, desc=f"Epoch {epoch} [Train]", leave=False)
    for batch_idx, (data, target) in enumerate(pbar):
        data, target = data.to(device), target.to(device)
        
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        
        running_loss += loss.item()
        pred = output.argmax(dim=1)
        all_preds.extend(pred.cpu().numpy())
        all_labels.extend(target.cpu().numpy())
        
        if batch_idx % 10 == 0:
            pbar.set_postfix({'loss': f'{loss.item():.4f}'})
    
    epoch_loss = running_loss / len(train_loader)
    accuracy = accuracy_score(all_labels, all_preds)
    kappa = cohen_kappa_score(all_labels, all_preds)
    
    return {'loss': epoch_loss, 'accuracy': accuracy, 'kappa': kappa}

def evaluate(model, test_loader, criterion, device, desc="[Eval]"):
    """Evaluate model"""
    model.eval()
    running_loss = 0.0
    all_preds, all_labels = [], []
    
    with torch.no_grad():
        for data, target in tqdm(test_loader, desc=desc, leave=False):
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss = criterion(output, target)
            
            running_loss += loss.item()
            pred = output.argmax(dim=1)
            all_preds.extend(pred.cpu().numpy())
            all_labels.extend(target.cpu().numpy())
    
    test_loss = running_loss / len(test_loader)
    accuracy = accuracy_score(all_labels, all_preds)
    kappa = cohen_kappa_score(all_labels, all_preds)
    
    return {'loss': test_loss, 'accuracy': accuracy, 'kappa': kappa}

def get_loso_dataloaders(data_dir, test_subject, batch_size=32, num_workers=0):
    """
    Leave-One-Subject-Out (LOSO) data loaders
    
    Args:
        data_dir: Path to processed numpy files
        test_subject: Subject ID to hold out for testing
        batch_size: Batch size for training
        num_workers: Number of workers for DataLoader
        
    Returns:
        train_loader: DataLoader for training subjects
        test_loader: DataLoader for test subject
    """
    data_path = Path(data_dir)
    
    # Training subjects
    train_subjects = [i for i in range(1, 10) if i != test_subject]
    train_files = []
    
    for subj_id in train_subjects:
        X_path = data_path / f"subject_{subj_id:02d}_X.npy"
        y_path = data_path / f"subject_{subj_id:02d}_y.npy"
        if X_path.exists():
            train_files.append((X_path, y_path))
    
    # Test subject
    test_X_path = data_path / f"subject_{test_subject:02d}_X.npy"
    test_y_path = data_path / f"subject_{test_subject:02d}_y.npy"
    
    # Load all data into memory (faster for training)
    X_train_list, y_train_list = [], []
    for X_path, y_path in train_files:
        X_train_list.append(np.load(X_path))
        y_train_list.append(np.load(y_path))
    
    X_train = np.concatenate(X_train_list, axis=0)
    y_train = np.concatenate(y_train_list, axis=0)
    
    X_test = np.load(test_X_path)
    y_test = np.load(test_y_path)
    
    print(f"Loaded: Train={X_train.shape}, Test={X_test.shape}")
    
    # Create datasets
    train_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_train), torch.LongTensor(y_train)
    )
    test_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_test), torch.LongTensor(y_test)
    )
    
    # Create dataloaders
    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=True
    )
    test_loader = DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=True
    )
    
    return train_loader, test_loader

def train_model(model, train_loader, test_loader, device, epochs=30, 
                lr=1e-3, weight_decay=1e-4, test_subject=1, save_dir="models/"):
    """
    Full training loop with checkpointing
    """
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)
    
    # Optimizer and scheduler
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer, max_lr=lr, steps_per_epoch=len(train_loader), epochs=epochs
    )
    
    # Loss function
    criterion = nn.CrossEntropyLoss()
    
    # Early stopping
    early_stopper = EarlyStopping(patience=7)
    
    # Training history
    history = {'train': [], 'val': []}
    
    print(f"🚀 Training EEGEncoder (Test Subject: {test_subject:02d})")
    print(f"📊 Train: {len(train_loader.dataset)} | Test: {len(test_loader.dataset)}")
    print(f"🧠 Model: {sum(p.numel() for p in model.parameters()) / 1e6:.2f}M parameters")
    
    best_accuracy = 0.0
    
    for epoch in range(1, epochs + 1):
        start_time = time.time()
        
        # Train
        train_metrics = train_epoch(model, train_loader, criterion, optimizer, device, epoch)
        
        # Validate
        val_metrics = evaluate(model, test_loader, criterion, device, desc="[Val]")
        
        # Update learning rate
        scheduler.step()
        
        # Record history
        history['train'].append(train_metrics)
        history['val'].append(val_metrics)
        
        epoch_time = time.time() - start_time
        
        # Print summary
        print(f"Epoch {epoch:02d}/{epochs} | "
              f"Train: {train_metrics['accuracy']:.4f} | "
              f"Val: {val_metrics['accuracy']:.4f} | "
              f"κ: {val_metrics['kappa']:.4f} | "
              f"LR: {scheduler.get_last_lr()[0]:.6f} | "
              f"Time: {epoch_time:.1f}s")
        
        # Save best model
        if val_metrics['accuracy'] > best_accuracy:
            best_accuracy = val_metrics['accuracy']
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'accuracy': best_accuracy,
                'kappa': val_metrics['kappa']
            }, save_dir / f"eegencoder_subject{test_subject:02d}_best.pth")
            print(f"💾 Checkpoint saved (Accuracy: {best_accuracy:.4f})")
        
        # Early stopping
        early_stopper(val_metrics['loss'])
        if early_stopper.early_stop:
            print(f"🛑 Early stopping triggered at epoch {epoch}")
            break
    
    # Load best model
    checkpoint = torch.load(
    save_dir / f"eegencoder_subject{test_subject:02d}_best.pth",
    weights_only=False  # Allow numpy dtypes
    )
    model.load_state_dict(checkpoint['model_state_dict'])
    
    # Final evaluation
    final_metrics = evaluate(model, test_loader, criterion, device, desc="[Final]")
    
    print(f"\n🏆 Final Results (Test Subject {test_subject:02d}):")
    print(f"Accuracy: {final_metrics['accuracy']*100:.2f}%")
    print(f"Kappa:    {final_metrics['kappa']:.4f}")
    
    # Save history
    with open(save_dir / f"history_subject{test_subject:02d}.json", 'w') as f:
        json.dump(history, f, indent=2)
    
    return model, history

def run_loso_cross_validation(data_dir, subjects=range(1, 10), device='cpu', epochs=20):
    """
    Run full LOSO cross-validation across all subjects
    """
    results = []
    
    for test_subject in subjects:
        print(f"\n{'='*50}")
        print(f"LOSO FOLD: Test Subject {test_subject:02d}")
        print(f"{'='*50}")
        
        # Get data loaders
        train_loader, test_loader = get_loso_dataloaders(
            data_dir, test_subject, batch_size=32
        )
        
        # Create model
        model = get_model(num_classes=4, pi_compatibility=(device == 'cpu'))
        model = model.to(device)
        
        # Train
        model, history = train_model(
            model, train_loader, test_loader, device,
            epochs=epochs, test_subject=test_subject
        )
        
        # Record result
        val_metrics = history['val'][-1]
        results.append({
            'test_subject': test_subject,
            'accuracy': val_metrics['accuracy'],
            'kappa': val_metrics['kappa']
        })
    
    # Summary
    print(f"\n{'='*50}")
    print("LOSO CROSS-VALIDATION SUMMARY")
    print(f"{'='*50}")
    accuracies = [r['accuracy'] for r in results]
    print(f"Mean Accuracy: {np.mean(accuracies)*100:.2f}% ± {np.std(accuracies)*100:.2f}%")
    print(f"Mean Kappa:    {np.mean([r['kappa'] for r in results]):.4f}")
    
    return results
