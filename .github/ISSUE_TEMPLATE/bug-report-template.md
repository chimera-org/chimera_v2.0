---
name: "🐛 Bug Report"
about: "Report a reproducible bug or regression in Chimera"
title: "[BUG]: "
labels: ["type: bug", "status: needs-triage", "priority: pending"]
assignees: ""
---
<!--
🔴 CRITICAL REMINDER 🔴
Before submitting, please ensure you've completed the following:
- Searched existing issues to avoid duplicates
- Completed ALL sections of this template
- Removed any sensitive/confidential information
- Attached necessary logs and screenshots
- Verified the issue with the latest version of Chimera
Incomplete bug reports may be deprioritized or closed.
-->
# 🐛 Bug Report
## 📋 Issue Summary
<!--Provide a clear, concise summary of the issue-->
**Chimera Component(s) Affected:**
<!--Specify which part(s) of Chimera are affected (e.g., Data Processing, Signal Analysis, Model Training, Inference, UI, etc.)-->

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
4. 

**Reproduction Rate:** <!--e.g., 100%, intermittent (30%), once only but consistently reproducible-->

**Time of First Occurrence:** <!--When did you first notice this issue? (YYYY-MM-DD)-->

## 💻 Environment Information
### System Details
| Information | Value |
|-------------|-------|
| Chimera Version | <!-- e.g., v2.0.1, commit hash if from source --> |
| Installation Method | <!-- e.g., from source, pip, poetry --> |
| Python Version | <!-- e.g., 3.9.7 (output of python --version) --> |
| Operating System | <!-- e.g., Ubuntu 22.04.1 LTS, Windows 11 Pro 21H2, macOS Monterey 12.5 --> |
| System Architecture | <!-- e.g., x86_64, ARM64, Apple Silicon --> |
| CPU Model | <!-- e.g., Intel Core i7-12700K, AMD Ryzen 9 5900X --> |
| Memory | <!-- e.g., 32GB DDR4 --> |
| GPU Model (if applicable) | <!-- e.g., NVIDIA RTX 3090, 24GB VRAM --> |
| CUDA/cuDNN Version (if applicable) | <!-- e.g., CUDA 11.7, cuDNN 8.4.1 --> |

### Development Environment
| Information | Value |
|-------------|-------|
| Editor/IDE | <!-- e.g., VS Code 1.70.2, PyCharm 2022.2 --> |
| Git Branch | <!-- e.g., main, develop, feature/xyz --> |
| Poetry Version (if used) | <!-- e.g., 1.2.1 --> |
| Virtual Environment | <!-- e.g., Poetry, venv, conda 4.14.0 --> |
| DVC Version (if used) | <!-- e.g., 2.10.1 --> |
| Hydra Version (if used) | <!-- e.g., 1.2.0 --> |
| CI/CD Environment (if applicable) | <!-- e.g., GitHub Actions, Jenkins, local --> |

### Hardware (if relevant)
| Information | Value |
|-------------|-------|
| EEG Device Model | <!-- e.g., Emotiv EPOC X --> |
| EEG Device Firmware | <!-- e.g., v3.2.1 --> |
| Exoskeleton Model | <!-- e.g., Model ABC-123 --> |
| Exoskeleton Firmware | <!-- e.g., v2.1.5 --> |
| Communication Protocol | <!-- e.g., Bluetooth 5.0, USB 3.0, Custom --> |
| Sensors | <!-- List any additional sensors relevant to the issue --> |
| Communication Latency | <!-- if relevant to the bug --> |

## ✅ Expected Behavior
<!--A clear and concise description of what you expected to happen-->

## ❌ Actual Behavior
<!--A clear description of what actually happened instead-->

### Error Messages
<!--If applicable, paste COMPLETE error messages, stack traces, or logs showing the error-->
<details>
<summary>Error Details (click to expand)</summary>

```
<!-- Paste the complete error message and stack trace here -->
```
</details>

## 📊 Logs and Output
<details>
<summary>Application Logs (click to expand)</summary>

```
<!-- Paste application logs here -->
```
</details>

<details>
<summary>Command Output (click to expand)</summary>

```bash
# Command executed:
<!-- Paste the exact command you ran -->

# Output:
<!-- Paste the command output here -->
```
</details>

<details>
<summary>System Logs (click to expand)</summary>

```
<!-- Paste any relevant system logs (e.g., dmesg, syslog) -->
```
</details>

## 📁 Configuration
<details>
<summary>Hydra Configuration (click to expand)</summary>

```yaml
<!-- Paste your Hydra configuration files here -->
```
</details>

<details>
<summary>Environment Variables (click to expand)</summary>

```
<!-- List relevant environment variables (no secrets/tokens) -->
```
</details>

<details>
<summary>Dependencies (click to expand)</summary>

```
<!-- Paste output of `poetry show` or `pip freeze` here -->
```
</details>

## 📊 Data & Models
**Data Characteristics:**

**Model Information:**

<details>
<summary>Data Sample (click to expand)</summary>

```
<!-- If possible, include a minimal anonymized data sample that reproduces the issue -->
<!-- For larger files, please provide a link to where the sample can be accessed -->
```
</details>

## 📷 Screenshots / Visualizations

## 🔍 Investigation Already Performed
**Things I've already tried:**
1. 
2. 
3. 

**Workaround (if any):**

## 📈 Regression Information
**Last known working version:**

**Changes that may have introduced this bug:**

**Related Issues/PRs:**

## 💻 Code Snippets
<details>
<summary>Relevant Code (click to expand)</summary>

```python
# Insert minimal code example that demonstrates the issue
```
</details>

## 🧪 Possible Tests

## 💡 Proposed Solution

## 📊 Impact Assessment
**Business Impact:**

**Number of Users Affected:**

**Performance Impact:**

**Security Implications:**

## 🔄 Reproducible Test Case

## ✅ Verification Steps

## 📝 Additional Notes

## ✅ Checklist
* [ ] I have searched existing issues to avoid creating a duplicate
* [ ] I have tested with the latest version of Chimera
* [ ] I have included complete error messages and stack traces
* [ ] I have provided detailed reproduction steps
* [ ] I have included relevant configuration files
* [ ] I have sanitized logs and configs to remove sensitive information
* [ ] I have included relevant screenshots or visualizations
* [ ] I have verified this is not an environment-specific issue
* [ ] I have run diagnostic tests (specify which ones)
* [ ] I have checked the documentation for relevant information
* [ ] I have labeled this issue with appropriate severity
* [ ] I have suggested possible solutions or workarounds
* [ ] I can help test fixes for this issue
* [ ] I understand complex bugs might require additional information
