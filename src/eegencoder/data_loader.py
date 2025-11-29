"""
BCI Competition IV 2a Data Loader
Compatible with MNE's string-based event handling
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
        self.trial_length = 4  # MI period
        
    def load_subject(self, subject_id, training=True):
        suffix = 'T' if training else 'E'
        filename = f"{self.data_path}A{subject_id:02d}{suffix}.gdf"
        
        raw = read_raw_gdf(filename, preload=True, verbose=False)
        raw.pick_channels(raw.ch_names[:self.n_channels])
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Get events (returns string-based annotation mapping)
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # BCI IV 2a event codes in GDF: 769, 770, 771, 772
        # Use STRING keys for event_id (MNE requirement for GDF)
        event_id = {
            '769': 1,  # left_hand
            '770': 2,  # right_hand
            '771': 3,  # foot
            '772': 4   # tongue
        }
        
        # CRITICAL: Do NOT subtract from events array
        # The integer codes in events[:, 2] map to annotation strings via event_dict
        # Just filter for motor imagery events using event_id
        
        print(f"DEBUG: Found events: {event_dict}")
        print(f"DEBUG: Selecting: {list(event_id.keys())}")
        
        # Epoch MI period (2s-6s = 4 seconds)
        epochs = Epochs(raw, events, event_id=event_id,
                       tmin=2.0, tmax=6.0, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop',
                       on_missing='ignore')  # Skip unknown events
        
        X = epochs.get_data()
        y = epochs.events[:, -1] - 1  # Convert 1-4 → 0-3
        
        print(f"✅ Final shape: {X.shape}, Labels: {len(y)}")
        return X, y

# Test function
def verify_dataset(loader, subject_id=1):
    print(f"\n🔍 Verifying Subject {subject_id:02d}...")
    X, y = loader.load_subject(subject_id)
    print(f"✅ Success: X={X.shape}, labels={np.bincount(y)}")
    return X, y

# Quick test
if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    X, y = verify_dataset(loader, subject_id=1)
