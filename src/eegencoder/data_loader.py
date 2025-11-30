# CELL: Test Corrected Loader
import sys
sys.path.append('/content/drive/MyDrive/chimera_v2.0/src')

from eegencoder.data_loader import BCIC4_2A_Loader

loader = BCIC4_2A_Loader("/content/drive/MyDrive/Motor_Imagery_Datasets/OpenBCI/BCI_cIV_2a/BCI_IV_2a/")

print("🔍 TESTING CORRECTED LOADER")
print("="*50)

for subj in [1, 2, 4, 9]:
    X, y = loader.load_subject(subj)
    print(f"Subject {subj}: {X.shape} | max_amp: {np.abs(X).max():.6f} V | labels: {np.bincount(y)}")
