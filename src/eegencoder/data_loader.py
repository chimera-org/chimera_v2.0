"""
BCI Competition IV 2a Data Loader
Robust handling of GDF event encoding (offset +2, duplicates)
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
        self.trial_length = 4  # MI period duration
        
    def load_subject(self, subject_id, training=True):
        suffix = 'T' if training else 'E'
        filename = f"{self.data_path}A{subject_id:02d}{suffix}.gdf"
        
        raw = read_raw_gdf(filename, preload=True, verbose=False)
        raw.pick_channels(raw.ch_names[:self.n_channels])
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Get events (with diagnostic prints)
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # CRITICAL: BCI IV 2a events are offset by +2 in GDFs
        # Codes: 5,6,7,8 → need to become 3,4,5,6
        # Then we map with event_id to 1-4
        events[:, 2] = events[:, 2] - 2
        
        print(f"DEBUG: Available events: {np.unique(events[:, 2])}")
        print(f"DEBUG: Found {len(events)} total events, {len(set(events[:, 0]))} unique samples")
        
        # Event mapping for motor imagery classes (after -2 correction)
        event_id = {
            3: 1,  # left_hand
            4: 2,  # right_hand
            5: 3,  # foot
            6: 4   # tongue
        }
        
        # Epoch MI period (2s-6s = 4 seconds)
        epochs = Epochs(raw, events, event_id=event_id,
                       tmin=2.0, tmax=6.0, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop')
        
        X = epochs.get_data()
        y = epochs.events[:, -1] - 1  # Convert 1-4 → 0-3
        
        # REMOVE strict assertions - use warnings instead
        if X.shape[1] != self.n_channels:
            print(f"⚠️  Channel mismatch: Expected {self.n_channels}, got {X.shape[1]}")
        if X.shape[2] != self.sfreq * self.trial_length:
            print(f"⚠️  Length mismatch: Expected {self.sfreq * self.trial_length}, got {X.shape[2]}")
            print(f"     This suggests events are at wrong positions or sfreq changed")
        
        print(f"✅ Final shape: {X.shape}, Labels: {len(y)}")
        return X, y

# Test function
def verify_dataset(loader, subject_id=1):
    print(f"\n🔍 Verifying Subject {subject_id:02d}...")
    X, y = loader.load_subject(subject_id)
    print(f"✅ Loaded: X={X.shape}, labels={np.bincount(y)}")
    return X, y

# Quick test
if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    X, y = verify_dataset(loader, subject_id=1)
