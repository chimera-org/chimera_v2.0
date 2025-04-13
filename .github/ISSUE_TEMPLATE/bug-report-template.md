---
name: "🐛 Bug Report"
about: "Report a reproducible bug or regression in Chimera"
title: "[BUG]: "
labels: ["type: bug", "status: needs-triage"]
assignees: ""
---
<!--
🔴 CRITICAL REMINDER 🔴
Before submitting, please ensure you've completed the following:
- Searched existing issues to avoid duplicates
- Completed ALL required sections of this template
- Removed any sensitive/confidential information
- Verified the issue with the latest version of Chimera
Incomplete bug reports may be closed without investigation.
-->
# 🐛 Bug Report
## 📋 Issue Summary
<!--Provide a clear, concise summary of the issue-->

**Chimera Component(s) Affected:**
<!--Specify which part(s) of Chimera are affected (e.g., Data Preprocessing, Feature Engineering, Model Architecture, Training Pipeline, Inference, Evaluation Metrics, etc.)-->

**Severity:**
<!--Choose one and delete the others-->
- 🔴 Critical (System crash, data loss, security vulnerability)
- 🟠 High (Major feature broken, no workaround)
- 🟡 Medium (Feature partially broken, workaround exists)
- 🟢 Low (Minor issue, cosmetic, trivial)

## 🔄 Reproduction Steps
<!--Provide detailed, step-by-step instructions to reproduce the issue. Be as specific as possible.-->
1. 
2. 
3. 

**Reproduction Rate:** <!--e.g., 100%, intermittent (30%)-->
**Environment:** <!--e.g., Local, Google Colab, AWS SageMaker, etc.-->

## 💻 Environment Information
| Information | Value |
|-------------|-------|
| Chimera Version | <!-- e.g., v2.0.1, commit hash if from source --> |
| Python Version | <!-- e.g., 3.9.7 --> |
| Operating System | <!-- e.g., Ubuntu 22.04, macOS 13.4 --> |
| GPU Model (if applicable) | <!-- e.g., NVIDIA RTX 3090 --> |

### ML Environment
| Information | Value |
|-------------|-------|
| ML Framework | <!-- e.g., PyTorch 2.0.1, TensorFlow 2.12.0 --> |
| Key Libraries | <!-- e.g., transformers 4.28.1, scikit-learn 1.2.2 --> |
| CUDA/cuDNN | <!-- e.g., CUDA 11.7, cuDNN 8.5 --> |
| Training Device | <!-- e.g., A100 GPU, CPU only, TPU v3-8 --> |

## ✅ Expected Behavior
<!--A clear and concise description of what you expected to happen-->

## ❌ Actual Behavior
<!--A clear description of what actually happened instead-->

<details>
<summary>Error Messages (click to expand)</summary>

```
<!-- Paste the complete error message and stack trace here -->
```
</details>

## 📊 Data & Model Information
**Dataset:** <!-- Name or brief description of dataset -->
**Model:** <!-- Model architecture or configuration -->
**Problem Type:** <!-- Classification, regression, generation, etc. -->

<details>
<summary>Model Config (click to expand)</summary>

```yaml
<!-- Paste relevant model configuration here -->
```
</details>

<details>
<summary>Data Sample (click to expand)</summary>

```
<!-- If possible, include a minimal anonymized data sample -->
```
</details>

## 🔍 Troubleshooting Information
<details>
<summary>Logs (click to expand)</summary>

```
<!-- Paste relevant logs here -->
```
</details>

**Attempted Solutions:**
<!-- List what you've already tried to resolve the issue -->
1. 
2. 

**Workaround (if any):**
<!-- Describe any temporary workaround you've found -->

## 📝 Additional Context
<!--Any other information that might be helpful for understanding the issue-->

## ✅ Checklist
* [ ] I have searched existing issues to avoid creating a duplicate
* [ ] I have verified this issue with the latest version of Chimera
* [ ] I have provided clear reproduction steps
* [ ] I have included error messages/stack traces (if applicable)
* [ ] I have included model and data information
* [ ] I have sanitized any sensitive information
