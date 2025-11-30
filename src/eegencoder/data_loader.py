"""
BCI Competition IV 2a Data Loader
Motor Imagery EEG Dataset Loader for EEGEncoder
"""

import numpy as np
import torch
from pathlib import Path
import mne
from mne.io import read_raw_gdf
from mne import events_from_annotations, Epochs
from torch.utils.data import Dataset, DataLoader
import warnings
warnings.filterwarnings('ignore')

class BCIC4_2A_Loader:
    """
    Corrected BCI IV 2a data loader
    - Fixes event extraction (gets 288 trials per subject)
    - Includes both load_subject AND load_all_subjects
    """
    
    def __init__(self, data_path="./data/bcic4_2a_raw/"):
        self.data_path = Path(data_path)
    
    def load_subject(self, subject_id, return_raw=False):
        """
        Load single subject with CORRECT event extraction
        """
        if not 1 <= subject_id <= 9:
            raise ValueError("subject_id must be between 1 and 9")
        
        gdf_file = self.data_path / f"A{subject_id:02d}T.gdf"
        raw = mne.io.read_raw_gdf(gdf_file, preload=True, verbose=False)
        
        events, event_id = mne.events_from_annotations(raw, verbose=False)
        
        # Map MI events (769-772) to 0-3
        mi_codes = {}
        for event_name, code in event_id.items():
            if event_name in ['769', '770', '771', '772']:
                mi_codes[code] = int(event_name) - 769
        
        mi_events = events[np.isin(events[:, 2], list(mi_codes.keys()))]
        
        epochs = mne.Epochs(raw, mi_events, event_id=mi_codes,
                            tmin=0, tmax=4.0, baseline=None, preload=True, verbose=False)
        
        X = epochs.get_data()
        y = epochs.events[:, -1]
        
        print(f"✅ Subject {subject_id:02d}: X={X.shape}, labels={np.bincount(y)}")
        
        if return_raw:
            return X, y, raw, epochs
        return X, y
    
    def load_all_subjects(self, subject_ids=None, training=True):
        """
        Load multiple subjects with trial tracking
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
        else:
            return X, y

# Helper function for LOSO
def get_loso_dataloaders(data_dir, test_subject, batch_size=32):
    from eegencoder.data_loader import BCIC4_2A_Loader
    
    loader = BCIC4_2A_Loader(data_dir)
    train_subjects = [i for i in range(1, 10) if i != test_subject]
    
    X_train, y_train, _ = loader.load_all_subjects(train_subjects, training=True)
    X_test, y_test, _ = loader.load_all_subjects([test_subject], training=False)
    
    train_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_train), torch.LongTensor(y_train)
    )
    test_dataset = torch.utils.data.TensorDataset(
        torch.FloatTensor(X_test), torch.LongTensor(y_test)
    )
    
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"Loaded: Train={X_train.shape}, Test={X_test.shape}")
    return train_loader, test_loader
