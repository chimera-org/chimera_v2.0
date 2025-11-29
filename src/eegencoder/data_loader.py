"""
BCI Competition IV 2a Data Loader
Optimized for Raspberry Pi deployment (minimal dependencies)
"""

import numpy as np
import scipy.io as sio
from mne.io import read_raw_gdf
from mne import events_from_annotations, Epochs
import warnings
warnings.filterwarnings('ignore')

class BCIC4_2A_Loader:
    """
    Minimal loader for BCI Competition IV dataset 2a
    Returns NumPy arrays directly (no MNE objects for Pi compatibility)
    """
    
    def __init__(self, data_path="/content/drive/MyDrive/BCI_IV_2a/"):
        """
        Args:
            data_path: Path to folder containing A01T.gdf, A01E.gdf, etc.
        """
        self.data_path = data_path
        self.sfreq = 250  # Sampling frequency (Hz)
        self.n_channels = 22  # EEG channels only (excluding 3 EOG)
        self.n_trials = 288
        self.trial_length = 4  # seconds
        
        # Event codes: corrected for BCI IV 2a
        self.event_id = {
            'left_hand': 1,
            'right_hand': 2,
            'foot': 3,
            'tongue': 4
        }
        
        # EEG channel names (22 channels)
        self.eeg_channels = [
            'Fz', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4', 'C5', 'C3', 'C1', 'Cz',
            'C2', 'C4', 'C6', 'CP3', 'CP1', 'CPz', 'CP2', 'CP4', 'P1', 'Pz',
            'P2', 'POz'
        ]
        
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
        
        # CRITICAL: Pick only EEG channels (first 22)
        # The raw file has 25 channels: 22 EEG + 3 EOG (last 3)
        raw.pick_channels(self.eeg_channels)
        
        # Apply bandpass filter (4-38 Hz) - critical for motor imagery
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Extract events (trial markers)
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # BCI IV 2a specific: event codes are offset by 2 in the file
        events[:, 2] = events[:, 2] - 2
        
        # Create epochs (trials)
        # tmin=0 (cue onset), tmax=4 (4 seconds after cue)
        epochs = Epochs(raw, events, event_id=self.event_id,
                       tmin=0, tmax=4, baseline=None,
                       preload=True, verbose=False)
        
        # Convert to NumPy arrays
        X = epochs.get_data()  # Shape: (n_trials, 22, 1000)
        y = epochs.events[:, -1] - 1  # Convert to 0-indexed labels
        
        # Basic sanity checks
        assert X.shape[1] == self.n_channels, f"Expected {self.n_channels} channels, got {X.shape[1]}"
        assert X.shape[2] == self.sfreq * self.trial_length, "Trial length mismatch"
        
        return X, y
    
    def load_all_subjects(self, subject_ids=None, training=True):
        """
        Load multiple subjects for cross-subject training
        
        Args:
            subject_ids: List of subject IDs (1-9). If None, loads all.
            training: Bool (True for training, False for evaluation)
            
        Returns:
            X: np.array (n_subjects * n_trials, n_channels, n_samples)
            y: np.array (n_subjects * n_trials,)
            groups: np.array (n_subjects * n_trials,) - Subject ID for each trial
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


# Quick sanity check function
def verify_dataset(loader, subject_id=1):
    """Load one subject and print diagnostics"""
    X, y = loader.load_subject(subject_id)
    
    print(f"✅ Subject {subject_id:02d} loaded successfully")
    print(f"📊 Data shape: {X.shape} (trials × channels × timepoints)")
    print(f"🏷️  Label distribution: {np.bincount(y)}")
    print(f"⚡ Data range: [{X.min():.2f}, {X.max():.2f}] µV")
    print(f"📈 Mean amplitude: {X.mean():.2f} ± {X.std():.2f} µV")
    
    return X, y
