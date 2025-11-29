"""
BCI Competition IV 2a Data Loader
Correct string-based event handling throughout
"""

import numpy as np
from mne.io import read_raw_gdf
from mne import events_from_annotations, Epochs
import warnings
warnings.filterwarnings('ignore')

class BCIC4_2A_Loader:
    def __init__(self, data_path="/content/drive/MyDrive/BCI_IV_2a/"):
        self.data_path = data_path
        self.sfreq = 250
        self.n_channels = 22
        self.n_trials = 288
        self.trial_length = 4
        
    def load_subject(self, subject_id, training=True):
        suffix = 'T' if training else 'E'
        filename = f"{self.data_path}A{subject_id:02d}{suffix}.gdf"
        
        raw = read_raw_gdf(filename, preload=True, verbose=False)
        raw.pick(raw.ch_names[:self.n_channels])
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Get events and mapping
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # DEBUG
        print(f"  Event mapping: {event_dict}")
        
        # Use string-based event_id (MNE requires this for GDF)
        event_id = {
            '769': 0,  # left_hand → label 0
            '770': 1,  # right_hand → label 1
            '771': 2,  # foot → label 2
            '772': 3   # tongue → label 3
        }
        
        # Create epochs - MNE maps strings to internal codes automatically
        epochs = Epochs(raw, events, event_id=event_id,
                       tmin=2.0, tmax=6.0, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop')
        
        X = epochs.get_data()
        y = epochs.events[:, -1]  # Already 0-3 from event_id mapping
        
        # Fix length
        if X.shape[2] == 1001:
            X = X[:, :, :1000]
        
        assert X.shape == (self.n_trials, self.n_channels, self.sfreq * self.trial_length)
        print(f"  ✅ Loaded: X={X.shape}, labels={np.bincount(y)}")
        return X, y

def verify_dataset(loader, subject_id=1):
    print(f"\n🔍 Verifying Subject {subject_id:02d}...")
    X, y = loader.load_subject(subject_id)
    return X, y

if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    X, y = verify_dataset(loader, subject_id=1)
