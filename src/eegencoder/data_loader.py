import numpy as np
from pathlib import Path
import mne
import torch

class BCIC4_2A_Loader:
    def __init__(self, data_path="./data/bcic4_2a_raw/"):
        self.data_path = Path(data_path)
    
    def load_subject(self, subject_id, return_raw=False):
        """
        FIXED: Load exact 288 trials per subject from BCI IV 2a dataset
        """
        if not (1 <= subject_id <= 9):
            raise ValueError(f"subject_id must be 1-9, got {subject_id}")
        
        gdf_file = self.data_path / f"A{subject_id:02d}T.gdf"
        raw = mne.io.read_raw_gdf(gdf_file, preload=True, verbose=False)
        
        # Extract events - CRITICAL: Use only CUE markers
        events, event_id = mne.events_from_annotations(raw, verbose=False)
        
        # BCI IV 2a uses these exact codes for motor imagery
        mi_event_map = {
            '769': 0,  # Left hand
            '770': 1,  # Right hand
            '771': 2,  # Foot
            '772': 3,  # Tongue
        }
        
        # Convert event names to codes
        mi_codes = {}
        for event_name, mi_label in mi_event_map.items():
            if event_name in event_id:
                code = event_id[event_name]
                mi_codes[code] = mi_label
        
        # Filter to only MI events
        mi_events = events[np.isin(events[:, 2], list(mi_codes.keys()))]
        
        # Create epochs (4 seconds at 250Hz = 1000 samples)
        epochs = mne.Epochs(raw, mi_events, event_id=mi_codes,
                            tmin=0, tmax=4.0, baseline=None, preload=True, verbose=False)
        
        if len(epochs) != 288:
            print(f"⚠️ WARNING: Subject {subject_id} has {len(epochs)} trials (expected 288)")
        
        X = epochs.get_data()
        y = epochs.events[:, -1]
        
        print(f"✅ Subject {subject_id:02d}: X={X.shape}, labels={np.bincount(y)}")
        
        if return_raw:
            return X, y, raw, epochs
        return X, y
    
    def load_all_subjects(self, subject_ids=None):
        """Load multiple subjects"""
        if subject_ids is None:
            subject_ids = list(range(1, 10))
        
        X_list, y_list = [], []
        for subj_id in subject_ids:
            X, y = self.load_subject(subj_id)
            X_list.append(X)
            y_list.append(y)
        
        return np.concatenate(X_list, axis=0), np.concatenate(y_list, axis=0)

# LOSO helper
def get_loso_dataloaders(data_path, test_subject, batch_size=32):
    """
    Fixed LOSO dataloaders
    """
    from eegencoder.data_loader import BCIC4_2A_Loader
    
    loader = BCIC4_2A_Loader(data_path)
    
    # Training subjects
    train_subjects = [i for i in range(1, 10) if i != test_subject]
    X_train, y_train = loader.load_all_subjects(train_subjects)
    
    # Test subject
    X_test, y_test = loader.load_subject(test_subject)
    
    # Convert to tensors
    train_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_train), torch.LongTensor(y_train)
    )
    test_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_test), torch.LongTensor(y_test)
    )
    
    # Create loaders
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"✅ LOSO prepared: Train={X_train.shape}, Test={X_test.shape}")
    
    return train_loader, test_loader
