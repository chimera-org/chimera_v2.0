"""
EEGEncoder Model - DSTS (Dual-Stream Temporal-Spatial) Architecture
Optimized for BCIC4_2a dataset: 22 channels, 250Hz, 4.5s trials
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional

class DownsamplingProjector(nn.Module):
    """Initial feature projection with aggressive downsampling for 250Hz input"""
    def __init__(self, in_channels: int = 22, target_dim: int = 128):
        super().__init__()
        # 1125 samples → ~281 samples after downsampling
        self.conv_blocks = nn.Sequential(
            nn.Conv1d(in_channels, 64, kernel_size=15, stride=3, padding=7),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, target_dim, kernel_size=11, stride=2, padding=5),
            nn.BatchNorm1d(target_dim),
            nn.ReLU()
        )
    
    def forward(self, x):
        return self.conv_blocks(x)  # (B, 128, ~281)

class StableTransformerEncoder(nn.Module):
    """Memory-efficient transformer with pre-norm (Raspberry Pi friendly)"""
    def __init__(self, dim: int, num_heads: int = 4, dropout: float = 0.2):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)
        self.norm2 = nn.LayerNorm(dim)
        self.attention = nn.MultiheadAttention(
            dim, num_heads, dropout=dropout, batch_first=True
        )
        self.ffn = nn.Sequential(
            nn.Linear(dim, dim * 2),  # Reduced expansion for Pi
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(dim * 2, dim)
        )
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        # Pre-norm for stability
        attn_out, _ = self.attention(x, x, x)
        x = x + self.dropout(attn_out)
        x = self.norm1(x)
        
        ffn_out = self.ffn(x)
        x = x + self.dropout(ffn_out)
        x = self.norm2(x)
        return x

class DSTSBlock(nn.Module):
    """Dual-Stream Temporal-Spatial Block (Parallel TCN + Transformer)"""
    def __init__(self, in_dim: int, num_heads: int = 4, dropout: float = 0.2):
        super().__init__()
        # Temporal Convolutional Network branch
        self.tcn = nn.Sequential(
            # Depthwise separable for efficiency
            nn.Conv1d(in_dim, in_dim, kernel_size=5, padding=2, groups=in_dim),
            nn.Conv1d(in_dim, in_dim, kernel_size=1),  # Pointwise
            nn.BatchNorm1d(in_dim),
            nn.ReLU(),
            nn.Dropout(dropout)
        )
        
        # Stable Transformer branch
        self.transformer = StableTransformerEncoder(in_dim, num_heads, dropout)
        
        # Gated fusion (learnable weighting)
        self.gate = nn.Sequential(
            nn.Linear(in_dim * 2, in_dim),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        # TCN branch (local temporal features)
        tcn_out = self.tcn(x)
        
        # Transformer branch (global spatial context)
        x_transposed = x.permute(0, 2, 1)  # (B, T, C)
        transformer_out = self.transformer(x_transposed)
        transformer_out = transformer_out.permute(0, 2, 1)  # (B, C, T)
        
        # Gated fusion
        combined = torch.cat([tcn_out, transformer_out], dim=1)
        gate_weights = self.gate(combined.permute(0, 2, 1)).permute(0, 2, 1)
        
        # Weighted sum
        fused = gate_weights * tcn_out + (1 - gate_weights) * transformer_out
        return fused

class EEGEncoder(nn.Module):
    """Main EEGEncoder with parallel DSTS branches and multi-scale processing"""
    def __init__(
        self,
        num_classes: int = 4,
        num_eeg_channels: int = 22,
        num_branches: int = 4,  # Reduced for Pi efficiency
        transformer_layers: int = 2,
        dropout: float = 0.2
    ):
        super().__init__()
        self.num_branches = num_branches
        
        # Initial projection
        self.projector = DownsamplingProjector(num_eeg_channels, 128)
        
        # Parallel DSTS branches with progressive dropout
        self.branches = nn.ModuleList([
            nn.Sequential(
                nn.Dropout(dropout * (i + 1) / num_branches),  # Progressive dropout
                DSTSBlock(128, num_heads=4, dropout=dropout)
            ) for i in range(num_branches)
        ])
        
        # Cross-branch attention for information fusion
        self.cross_branch_attn = nn.MultiheadAttention(
            128, num_heads=4, dropout=dropout, batch_first=True
        )
        
        # Final transformer layers
        self.transformer_layers = nn.ModuleList([
            StableTransformerEncoder(128, num_heads=4, dropout=dropout)
            for _ in range(transformer_layers)
        ])
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool1d(1),  # Global average pooling
            nn.Flatten(),
            nn.Linear(128, 64),       # Reduced size for Pi
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(64, num_classes)
        )
        
    def forward(self, x):
        # Initial projection
        x = self.projector(x)  # (B, 128, T')
        
        # Parallel branches with residual connections
        branch_outputs = []
        for branch in self.branches:
            branch_out = branch(x)
            branch_outputs.append(branch_out + x)  # Residual
            
        # Stack and average branch outputs
        x = torch.stack(branch_outputs).mean(dim=0)
        
        # Cross-branch attention (model inter-branch relationships)
        x_attn = x.permute(0, 2, 1)  # (B, T, C)
        x_attn, _ = self.cross_branch_attn(x_attn, x_attn, x_attn)
        x = x + x_attn.permute(0, 2, 1)  # Residual
        
        # Final transformer processing
        x = x.permute(0, 2, 1)  # (B, T, C)
        for layer in self.transformer_layers:
            x = layer(x)
        
        # Classification
        x = x.permute(0, 2, 1)  # (B, C, T)
        return self.classifier(x)

def get_model(num_classes: int = 4, pi_compatibility: bool = True) -> EEGEncoder:
    """
    Factory function with Raspberry Pi optimizations
    pi_compatibility: If True, reduces model size for 4GB RAM Pi
    """
    if pi_compatibility:
        return EEGEncoder(
            num_classes=num_classes,
            num_branches=3,           # Reduced branches
            transformer_layers=1,     # Single final layer
            dropout=0.1
        )
    else:
        return EEGEncoder(num_classes=num_classes)

if __name__ == "__main__":
    # Model test
    model = get_model(num_classes=4, pi_compatibility=True)
    x = torch.randn(2, 22, 1125)  # BCIC4_2a input
    out = model(x)
    print(f"Input: {x.shape} → Output: {out.shape}")
    print(f"Parameters: {sum(p.numel() for p in model.parameters()) / 1e6:.2f}M")
