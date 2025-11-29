"""
BCI Competition IV 2a Data Loader
Correct event selection by numeric codes
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
        
        # DEBUG
        print(f"  Event mapping: {event_dict}")
        
        # Load all events, then filter by numeric codes
        all_epochs = Epochs(raw, events, event_id=None,
                           tmin=0, tmax=6, baseline=None,
                           preload=True, verbose=False,
                           event_repeated='drop')
        
        # Select motor imagery trials by internal codes
        # From your debug: '769':7, '770':8, '771':9, '772':10
        mi_epochs = all_epochs[7, 8, 9, 10]  # NUMERIC codes, not strings!
        
        X = mi_epochs.get_data()
        
        # Map internal codes to labels
        event_code_to_label = {7: 0, 8: 1, 9: 2, 10: 3}
        y = np.array([event_code_to_label[e] for e in mi_epochs.events[:, 2]])
        
        # Fix length off-by-one
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
