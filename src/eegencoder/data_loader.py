"""
BCI Competition IV 2a Data Loader
Fixed inst.pick() API and robust event filtering
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
        
        # FIXED: Use inst.pick() instead of pick_channels()
        raw.pick(raw.ch_names[:self.n_channels])
        
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Get all events
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # Filter motor imagery events (internal codes 7,8,9,10)
        mi_events = events[np.isin(events[:, 2], [7, 8, 9, 10])]
        
        # Create epochs with MI events only
        epochs = Epochs(raw, mi_events, event_id={7:1, 8:2, 9:3, 10:4},
                       tmin=2.0, tmax=6.0, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop')
        
        X = epochs.get_data()
        
        # Map internal codes to labels 0-3
        event_code_to_label = {7:0, 8:1, 9:2, 10:3}
        y = np.array([event_code_to_label[e] for e in epochs.events[:, 2]])
        
        # Trim to exactly 1000 samples (4s @ 250Hz)
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
