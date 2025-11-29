"""
BCI Competition IV 2a Data Loader
Motor Imagery EEG Dataset Loader for EEGEncoder
"""

import numpy as np
from mne.io import read_raw_gdf
from mne import events_from_annotations, Epochs
import warnings
warnings.filterwarnings('ignore')

class BCIC4_2A_Loader:
    """
    Robust loader for BCI Competition IV 2a dataset
    Handles: GDF format, 22 EEG channels, motor imagery events (769-772)
    Returns: (n_trials, 22, 1000) arrays with balanced labels (0-3)
    """
    
    def __init__(self, data_path="/content/drive/MyDrive/BCI_IV_2a/"):
        """
        Args:
            data_path: Path to folder with A01T.gdf, A01E.gdf, etc.
        """
        self.data_path = data_path
        self.sfreq = 250  # Sampling rate (Hz)
        self.n_channels = 22  # EEG channels (excludes 3 EOG)
        self.trial_length = 4  # Motor imagery duration (seconds)
        
    def load_subject(self, subject_id, training=True):
        """
        Load single subject's EEG trials
        
        Args:
            subject_id: Integer 1-9
            training: True for training session (T), False for evaluation (E)
            
        Returns:
            X: np.array (n_trials, 22, 1000) - EEG data
            y: np.array (n_trials,) - Labels (0=left, 1=right, 2=foot, 3=tongue)
        """
        suffix = 'T' if training else 'E'
        filename = f"{self.data_path}A{subject_id:02d}{suffix}.gdf"
        
        # Load and preprocess
        raw = read_raw_gdf(filename, preload=True, verbose=False)
        raw.pick(raw.ch_names[:self.n_channels])
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Extract events
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # Select motor imagery events only (internal codes 7,8,9,10)
        mi_codes = [event_dict['769'], event_dict['770'], 
                   event_dict['771'], event_dict['772']]
        mi_events = events[np.isin(events[:, 2], mi_codes)]
        
        # Create epochs (2s-6s = 4 second MI window)
        epochs = Epochs(raw, mi_events, event_id=None,
                       tmin=2.0, tmax=6.0, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop')
        
        # Get data and labels
        X = epochs.get_data()
        
        # Map event codes to labels 0-3
        code_to_label = {event_dict['769']:0, event_dict['770']:1, 
                        event_dict['771']:2, event_dict['772']:3}
        y = np.array([code_to_label[code] for code in epochs.events[:, 2]])
        
        # Ensure exact 4-second duration (1000 samples @ 250Hz)
        if X.shape[2] == 1001:
            X = X[:, :, :1000]
        
        return X, y
    
    def load_all_subjects(self, subject_ids=None, training=True):
        """
        Load multiple subjects for cross-subject training
        
        Args:
            subject_ids: List of subject IDs (1-9). If None, loads all.
            
        Returns:
            X: Concatenated data from all subjects
            y: Concatenated labels
            groups: Subject ID for each trial (for cross-validation)
        """
        if subject_ids is None:
            subject_ids = list(range(1, 10))
            
        X_list, y_list, groups_list = [], [], []
        
        for subj_id in subject_ids:
            X_subj, y_subj = self.load_subject(subj_id, training=training)
            X_list.append(X_subj)
            y_list.append(y_subj)
            groups_list.append([subj_id] * len(y_subj))
            
        X = np.concatenate(X_list, axis=0)
        y = np.concatenate(y_list, axis=0)
        groups = np.concatenate(groups_list, axis=0)
        
        return X, y, groups

def verify_dataset(loader, subject_id=1):
    """Quick verification function"""
    print(f"\n🔍 Verifying Subject {subject_id:02d}...")
    X, y = loader.load_subject(subject_id)
    print(f"✅ SUCCESS: X={X.shape}, labels={np.bincount(y)}")
    return X, y

if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    # Test first 3 subjects
    for subj_id in [1, 2, 3]:
        X, y = verify_dataset(loader, subject_id=subj_id)
