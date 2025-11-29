"""
BCI Competition IV 2a Data Loader
Handles dropped duplicate events
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
        self.n_trials = 288  # Expected, but actual may vary
        self.trial_length = 4
        
    def load_subject(self, subject_id, training=True):
        suffix = 'T' if training else 'E'
        filename = f"{self.data_path}A{subject_id:02d}{suffix}.gdf"
        
        raw = read_raw_gdf(filename, preload=True, verbose=False)
        raw.pick(raw.ch_names[:self.n_channels])
        raw.filter(l_freq=4, h_freq=38, method='iir', verbose=False)
        
        # Get events and mapping
        events, event_dict = events_from_annotations(raw, verbose=False)
        
        # Map annotations to internal codes
        mi_codes = [event_dict['769'], event_dict['770'], 
                   event_dict['771'], event_dict['772']]
        
        # Filter to MI events
        mi_selector = np.isin(events[:, 2], mi_codes)
        mi_events_original = events[mi_selector]
        
        # Create epochs (some duplicates may be dropped)
        epochs = Epochs(raw, mi_events_original, event_id=None,
                       tmin=2.0, tmax=6.0, baseline=None,
                       preload=True, verbose=False,
                       event_repeated='drop')
        
        X = epochs.get_data()
        
        # Map internal codes to labels
        code_to_label = {event_dict['769']:0, event_dict['770']:1, 
                        event_dict['771']:2, event_dict['772']:3}
        
        # EXTRACT labels - but only for events that survived
        # epochs.events contains the final events after dropping duplicates
        y = np.array([code_to_label[code] for code in epochs.events[:, 2]])
        
        # Fix length
        if X.shape[2] == 1001:
            X = X[:, :, :1000]
        
        # Final verification (no strict trial count)
        assert X.shape[1] == self.n_channels
        assert X.shape[2] == self.sfreq * self.trial_length
        assert len(y) == X.shape[0]  # Must match after trimming
        
        print(f"  ✅ SUCCESS: X={X.shape}, labels={np.bincount(y)}")
        return X, y

def verify_dataset(loader, subject_id=1):
    print(f"\n🔍 Verifying Subject {subject_id:02d}...")
    X, y = loader.load_subject(subject_id)
    return X, y

if __name__ == "__main__":
    loader = BCIC4_2A_Loader()
    X, y = verify_dataset(loader, subject_id=1)
