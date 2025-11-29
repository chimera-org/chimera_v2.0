"""
EEGEncoder Training Loop with Cross-Subject Validation
Supports both GPU and Raspberry Pi 4 CPU training
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix
import numpy as np
from tqdm import tqdm
import json
import time
from pathlib import Path
import os

class StreamingDataset(Dataset):
    """Memory-efficient dataset for Pi (loads from disk on demand)"""
    def __init__(self, data_dir, subject_ids, is_training=True, transform=None):
        self.data_dir = Path(data_dir)
        self.subject_ids = subject_ids
        self.is_training = is_training
        self.transform = transform
        self.filepaths = self._get_filepaths()
        
    def _get_filepaths(self):
        """Pre-compute all file paths to avoid disk scanning"""
        paths = []
        for subj_id in self.subject_ids:
            suffix = 'train' if self.is_training else 'eval'
            X_path = self.data_dir / f"subject_{subj_id:02d}_{suffix}_X.npy"
            y_path = self.data_dir / f"subject_{subj_id:02d}_{suffix}_y.npy"
            if X_path.exists():
                paths.append((X_path, y_path))
        return paths
    
    def __len__(self):
        return len(self.filepaths) * 288  # 288 trials per subject
    
    def __getitem__(self, idx):
        # Determine which subject file to load
        file_idx = idx // 288
        trial_idx = idx % 288
        
        X_path, y_path = self.filepaths[file_idx]
        
        # Load only the needed trial (memory efficient)
        X = np.load(X_path, mmap_mode='r')[trial_idx]
        y = np.load(y_path, mmap_mode='r')[trial_idx]
        
        if self.transform:
            X = self.transform(X)
            
        return torch.FloatTensor(X), torch.LongTensor([y])[0]

def get_loso_dataloaders(data_dir, test_subject, batch_size=32, num_workers=0):
    """
    Leave-One-Subject-Out (LOSO) cross-validation
    Returns train/test loaders for one fold
    """
    train_subjects = [i for i in range(1, 10) if i != test_subject]
    
    train_dataset = StreamingDataset(data_dir, train_subjects, is_training=True)
    test_dataset = StreamingDataset(data_dir, [test_subject], is_training=True)
    
    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=False  # pin_memory=False for Pi
    )
    
    test_loader = DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=False
    )
    
    return train_loader, test_loader

class LabelSmoothingCE(nn.Module):
    """Cross-Entropy with label smoothing (from paper)"""
    def __init__(self, num_classes=4, smoothing=0.1):
        super().__init__()
        self.smoothing = smoothing
        self.num_classes = num_classes
        
    def forward(self, pred, target):
        confidence = 1.0 - self.smoothing
        log_probs = torch.log_softmax(pred, dim=-1)
        
        with torch.no_grad():
            true_dist = torch.zeros_like(pred)
            true_dist.fill_(self.smoothing / (self.num_classes - 1))
            true_dist.scatter_(1, target.data.unsqueeze(1), confidence)
        
        return torch.mean(torch.sum(-true_dist * log_probs, dim=-1))

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
    """Train one epoch with progress bar"""
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
        
        # Gradient clipping for stability
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
    """Evaluate model and return metrics"""
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

def train_model(
    model,
    train_loader,
    test_loader,
    device,
    epochs=30,
    lr=1e-3,
    weight_decay=1e-4,
    save_dir="models/",
    test_subject=1
):
    """Full training loop with checkpointing"""
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)
    
    # Optimizer and scheduler
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=lr, weight_decay=weight_decay
    )
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer, max_lr=lr, steps_per_epoch=len(train_loader), epochs=epochs
    )
    
    # Loss function
    criterion = LabelSmoothingCE(num_classes=4, smoothing=0.1)
    
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
        
        # Print epoch summary
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
        
        # Early stopping check
        early_stopper(val_metrics['loss'])
        if early_stopper.early_stop:
            print(f"🛑 Early stopping triggered at epoch {epoch}")
            break
    
    # Load best model
    checkpoint = torch.load(save_dir / f"eegencoder_subject{test_subject:02d}_best.pth")
    model.load_state_dict(checkpoint['model_state_dict'])
    
    # Final evaluation with confusion matrix
    final_metrics = evaluate(model, test_loader, criterion, device, desc="[Final]")
    
    print(f"\n🏆 Final Results (Test Subject {test_subject:02d}):")
    print(f"Accuracy: {final_metrics['accuracy']*100:.2f}%")
    print(f"Kappa:    {final_metrics['kappa']:.4f}")
    
    # Save history
    with open(save_dir / f"history_subject{test_subject:02d}.json", 'w') as f:
        json.dump(history, f, indent=2)
    
    return model, history

def run_loso_cross_validation(data_dir, subjects=range(1, 10), device='cpu', epochs=20):
    """Run full LOSO cross-validation"""
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
        model = EEGEncoder(num_classes=4, pi_compatibility=(device == 'cpu'))
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
