import numpy as np
from pathlib import Path
import mne
import torch
from torch.utils.data import DataLoader, TensorDataset

class BCIC4_2A_Loader:
    """
    CORRECTED BCI IV 2a loader - extracts 288 trials per subject
    """
    
    def __init__(self, data_path="./data/bcic4_2a_raw/"):
        self.data_path = Path(data_path)
    
    def load_subject(self, subject_id, return_raw=False):
        """
        Load single subject with CORRECT event extraction
        Returns: X (288 trials, 22 channels, 1000 samples), y (0-3 labels)
        """
        if not 1 <= subject_id <= 9:
            raise ValueError(f"subject_id must be 1-9, got {subject_id}")
        
        # Load GDF file
        gdf_file = self.data_path / f"A{subject_id:02d}T.gdf"
        
        if not gdf_file.exists():
            raise FileNotFoundError(f"File not found: {gdf_file}")
        
        raw = mne.io.read_raw_gdf(gdf_file, preload=True, verbose=False)
        
        # Extract events
        events, event_id = mne.events_from_annotations(raw, verbose=False)
        
        # Map MI events (769-772) to labels 0-3
        # CRITICAL: Use the numeric codes from the GDF, not string names
        mi_codes = {}
        for code, label in event_id.items():
            if str(code) in ['769', '770', '771', '772']:  # String comparison
                mi_codes[label] = int(str(code)) - 769
        
        if not mi_codes:
            raise ValueError(f"No MI events found in {gdf_file}")
        
        # Filter events
        mi_events = events[np.isin(events[:, 2], list(mi_codes.keys()))]
        
        # Create epochs (4 seconds, no baseline)
        epochs = mne.Epochs(raw, mi_events, event_id=mi_codes,
                            tmin=0, tmax=4.0, baseline=None,
                            preload=True, verbose=False)
        
        # Get data
        X = epochs.get_data()
        y = epochs.events[:, -1]
        
        print(f"✅ Subject {subject_id:02d}: {X.shape}, labels={np.bincount(y)}")
        
        if return_raw:
            return X, y, raw, epochs
        return X, y
    
    def load_all_subjects(self, subject_ids=None, training=True):
        """
        Load multiple subjects
        """
        if subject_ids is None:
            subject_ids = list(range(1, 10))
        
        X_list, y_list, groups_list = [], [], []
        
        for subj_id in subject_ids:
            X_subj, y_subj = self.load_subject(subj_id)
            X_list.append(X_subj)
            y_list.append(y_subj)
            groups_list.append([subj_id] * len(y_subj))
        
        X = np.concatenate(X_list, axis=0)
        y = np.concatenate(y_list, axis=0)
        
        if training:
            groups = np.concatenate(groups_list, axis=0)
            return X, y, groups
        return X, y


# Helper function for LOSO
def get_loso_dataloaders(data_dir, test_subject, batch_size=32):
    """
    Create train/test loaders for LOSO cross-validation
    """
    from eegencoder.data_loader import BCIC4_2A_Loader
    
    loader = BCIC4_2A_Loader(data_dir)
    train_subjects = [i for i in range(1, 10) if i != test_subject]
    
    X_train, y_train, _ = loader.load_all_subjects(train_subjects, training=True)
    X_test, y_test, _ = loader.load_all_subjects([test_subject], training=False)
    
    # Convert to tensors
    train_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_train), torch.LongTensor(y_train)
    )
    test_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_test), torch.LongTensor(y_test)
    )
    
    # Create loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"Loaded: Train={X_train.shape}, Test={X_test.shape}")
    return train_loader, test_loader
