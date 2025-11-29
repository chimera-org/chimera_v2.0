"""
BCI Competition IV 2a Data Loader
Correct event mapping: Uses MNE's internal codes directly
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
        raw.pick_channels(raw.ch_names[:self.n_channels])
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Get events and their internal mapping
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # DEBUG: Show what we're working with
        print(f"  Event mapping: {event_dict}")
        
        # Load ALL epochs first (including markers, artifacts, etc.)
        # Use a broad event_id to capture everything, then filter
        all_epochs = Epochs(raw, events, event_id=None,  # Load ALL events
                           tmin=0, tmax=6, baseline=None,
                           preload=True, verbose=False,
                           event_repeated='drop')
        
        # Now select ONLY motor imagery trials by annotation
        # This uses string keys to select epochs (cleaner than numeric codes)
        mi_epochs = all_epochs['769', '770', '771', '772']
        
        X = mi_epochs.get_data()
        
        # Extract labels from epochs metadata
        # events array contains [sample, duration, event_code]
        # event_code for MI classes are 7,8,9,10 (from event_dict)
        # Map them to 0-3
        event_code_to_label = {7: 0, 8: 1, 9: 2, 10: 3}
        y = np.array([event_code_to_label[e] for e in mi_epochs.events[:, 2]])
        
        # Trim to exactly 4 seconds (handle off-by-one)
        if X.shape[2] == 1001:  # MNE sometimes gives extra sample
            X = X[:, :, :1000]
        elif X.shape[2] == 999:  # Or missing one
            X = np.pad(X, ((0,0), (0,0), (0,1)), mode='edge')
        
        # Final verification
        assert X.shape == (self.n_trials, self.n_channels, self.sfreq * self.trial_length), \
            f"Expected {(self.n_trials, self.n_channels, self.sfreq * self.trial_length)}, got {X.shape}"
        assert len(y) == self.n_trials, f"Expected {self.n_trials} trials, got {len(y)}"
        
        print(f"  ✅ Loaded: X={X.shape}, labels={np.bincount(y)}")
        return X, y

def verify_dataset(loader, subject_id=1):
    print(f"\n🔍 Verifying Subject {subject_id:02d}...")
    X, y = loader.load_subject(subject_id)
    print(f"🎯 Final: X={X.shape}, labels={np.bincount(y)}")
    return X, y

# Quick test
if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    X, y = verify_dataset(loader, subject_id=1)
