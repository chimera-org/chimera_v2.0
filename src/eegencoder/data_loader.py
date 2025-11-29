"""
BCI Competition IV 2a Data Loader
Robust event handling for duplicate time samples
"""

import numpy as np
from mne.io import read_raw_gdf
from mne import events_from_annotations, Epochs
import warnings
warnings.filterwarnings('ignore')

class BCIC4_2A_Loader:
    """
    Robust loader for BCI Competition IV dataset 2a
    Handles duplicate events and channel selection correctly
    """
    
    def __init__(self, data_path="/content/drive/MyDrive/BCI_IV_2a/"):
        """
        Args:
            data_path: Path to folder containing A01T.gdf, A01E.gdf, etc.
        """
        self.data_path = data_path
        self.sfreq = 250  # Sampling frequency (Hz)
        self.n_channels = 22  # EEG channels only
        self.n_trials = 288
        self.trial_length = 4  # seconds
        
        # Event codes for motor imagery tasks (corrected for BCI IV 2a)
        self.event_id = {
            'left_hand': 1,
            'right_hand': 2,
            'foot': 3,
            'tongue': 4
        }
        
    def load_subject(self, subject_id, training=True):
        """
        Load a single subject's data
        
        Args:
            subject_id: Integer 1-9
            training: Bool (True for training session, False for evaluation)
            
        Returns:
            X: np.array (n_trials, n_channels, n_samples) - EEG data
            y: np.array (n_trials,) - Labels (0-3)
        """
        suffix = 'T' if training else 'E'
        filename = f"{self.data_path}A{subject_id:02d}{suffix}.gdf"
        
        # Load raw GDF file
        raw = read_raw_gdf(filename, preload=True, verbose=False)
        
        # Select first 22 channels (EEG) and drop EOG
        eeg_channel_names = raw.ch_names[:self.n_channels]
        raw.pick(eeg_channel_names)
        
        # Apply bandpass filter (4-38 Hz) - critical for motor imagery
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Extract events from annotations
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # CRITICAL: BCI IV 2a event codes need correction
        # Raw events are offset by +2 (so class 1 is code 3, etc.)
        events[:, 2] = events[:, 2] - 2
        
        # Create epochs with robust event handling
        # event_repeated='drop' handles duplicate time samples
        # on_missing='ignore' prevents errors if some events are missing
        epochs = Epochs(raw, events, event_id=self.event_id,
                       tmin=0, tmax=self.trial_length, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop',  # Drop duplicates
                       on_missing='ignore')    # Skip missing events
        
        # Convert to NumPy arrays
        X = epochs.get_data()  # Shape: (n_trials, n_channels, n_samples)
        y = epochs.events[:, -1] - 1  # Convert to 0-indexed labels
        
        # Verify shape
        assert X.shape[1] == self.n_channels, f"Expected {self.n_channels} channels, got {X.shape[1]}"
        assert X.shape[2] == self.sfreq * self.trial_length, "Trial length mismatch"
        
        return X, y
    
    def load_all_subjects(self, subject_ids=None, training=True):
        """
        Load multiple subjects for cross-subject training
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
    """Load one subject and print diagnostics"""
    X, y = loader.load_subject(subject_id)
    
    print(f"✅ Subject {subject_id:02d} loaded successfully")
    print(f"📊 Data shape: {X.shape} (trials × channels × timepoints)")
    print(f"🏷️  Label distribution: {np.bincount(y)}")
    print(f"⚡ Data range: [{X.min():.2f}, {X.max():.2f}] µV")
    print(f"📈 Mean amplitude: {X.mean():.2f} ± {X.std():.2f} µV")
    
    return X, y

# Quick test
if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    X, y = verify_dataset(loader, subject_id=1)
    print(f"\nFinal verification: X.shape = {X.shape}")
