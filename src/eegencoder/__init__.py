"""
EEGEncoder Package
Motor Imagery EEG Classification using DSTS Architecture
"""

from .model import EEGEncoder, get_model
from .data_loader import BCIC4_2A_Loader, get_dataloaders
from .train import (
    train_model, 
    train_epoch, 
    evaluate, 
    get_loso_dataloaders, 
    run_loso_cross_validation
)

__version__ = "2.0.0"
__author__ = "Chimera Org"
__description__ = "EEGEncoder with Raspberry Pi optimization"
