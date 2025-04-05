# Chimera 🧠🦾 

<div align="center">

![Chimera Logo](https://img.shields.io/badge/-%F0%9F%A7%A0%20CHIMERA%20%F0%9F%A6%BE-6236FF?style=for-the-badge&labelColor=1A1A2E)

**Machine Learning for Mind-Controlled Exoskeletons**

[![Build Status](https://img.shields.io/github/actions/workflow/status/heya-vyom/chimera_v2.0/tests.yml?branch=main&style=flat-square&logo=github-actions&logoColor=white&label=CI)](https://github.com/heya-vyom/chimera_v2.0/actions/workflows/tests.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/heya-vyom/chimera_v2.0?style=flat-square&logo=codecov&logoColor=white)](https://codecov.io/gh/heya-vyom/chimera_v2.0)
[![License](https://img.shields.io/github/license/heya-vyom/chimera_v2.0?style=flat-square&logo=apache&logoColor=white)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square&logo=python&logoColor=white)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&logo=python&logoColor=white)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square)](https://github.com/pre-commit/pre-commit)
[![FDA Compliance](https://img.shields.io/badge/FDA-Compliance%20Ready-green?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJDNi41IDIgMiA2LjUgMiAxMnM0LjUgMTAgMTAgMTAgMTAtNC41IDEwLTEwUzE3LjUgMiAxMiAyem0tMSAxNkg3di0yaDR2MnptNi40LTRINi42Yy0uOSAwLTEuNi0uNy0xLjYtMS42VjYuNkM1IDUuNyA1LjcgNSA2LjYgNWgxMC44Yy45IDAgMS42LjcgMS42IDEuNnY1LjhjMCAuOS0uNyAxLjYtMS42IDEuNnoiIGZpbGw9IndoaXRlIi8+PC9zdmc+)](regulatory/fda_strategy.md)

</div>

## 📋 Overview

Chimera is a comprehensive machine learning platform for brain-controlled exoskeletons, designed to restore mobility for individuals with quadriplegia. The platform processes Electroencephalography (EEG) signals to decode movement intentions and translate them into precise exoskeleton control commands.

<div align="center">
<img src="https://mermaid.ink/img/pako:eNp1kU9PwzAMxb9KlBOI9QvkMG3qBBJiB8QOvUQmMY3WJlWSMjZV_e7YbVlhwJf4-fez_OzCuJUEBbwQb8lYvGvDLZIVUXxA8t5ZJA_WkVYRXdA6JGQvVkWUhLxGRWQMqQhXZJV3pCNcxHmcx1mcx_9i5_uoI1zGeZzHeZzH-b_YRYRXcR7ncR7ncR7nMXZ-jjrCdZzHeZzHeZzHeYyd36KO8C7O4zzO4zzO4zzGzh9RR_gY53Ee53Ee53EeY-fPqCP8ivM4j_M4j_M4j7HzLuoIf-I8zuM8zuM8zmPs_Bt1hMc4j_M4j_M4j_MYO0-ijvAU53Ee53Ee53EeY-c0wlOcx3mcx3mcx3mMnbMIT3Ee53Ee53Ee5zF2ziM8xXmcx3mcx3mcx9i5iPAU53Ee53Ee53EeY-cywnOcx3mcx3mcx3mMnasIz3Ee53Ee53Ee5zF2riO8xHmcx3mcx3mcx9i5ifAS53Ee53Ee53EeY-c2wkucx3mcx3mcx3mMnbsIL3Ee53Ee53Ee5zF27iO8xnmcx3mcx3mcx9h5iPAa53Ee53Ee53EeY-cxwmucx3mcx3mcx3mMnacIb3Ee53Ee53Ee5zF2niO8xXmcx3mcx3mcx9h5ifAW53Ee53Ee53EeY-c1wlucx3mcx3mcx3mMnbcI73Ee53Ee53Ee5zF23iO8x3mcx3mcx3mcx9j5iPAe53Ee53Ee53EeY-czwnucx3mcx3mcx3mMna8IH3Ee53Ee53Ee5zF2viN8xHmcx3mcx3mcx9j5ifAR53Ee53Ee53EeY-e_CB9xHudxHudxHucxdv4HxvXwKQ?type=png" alt="Chimera System Architecture" width="700px" />
</div>

Chimera encompasses the entire ML pipeline from raw data ingestion and preprocessing to model training, evaluation, and deployment-ready inference logic. It is designed with regulatory compliance in mind, following FDA guidelines for Software as a Medical Device (SaMD) with AI/ML components.

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔄 End-to-End EEG Pipeline

- **Data Loading**: Flexible data ingestion from various EEG devices
- **Signal Processing**: Robust filtering, artifact removal, and preprocessing
- **Feature Extraction**: CSP, PSD, and advanced feature engineering
- **Dataset Creation**: Standardized dataset preparation for ML models

</td>
<td width="50%">

### 🧠 Flexible Modeling

- **Classical ML**: LDA, SVM, and other traditional approaches
- **Deep Learning**: EEGNet, ShallowConvNet, and custom architectures
- **Framework Support**: PyTorch and TensorFlow integration
- **Transfer Learning**: Cross-subject and cross-session adaptation

</td>
</tr>
<tr>
<td>

### ⚙️ Configuration Driven

- **Hydra Integration**: Complex configuration management
- **Experiment Tracking**: MLflow / Weights & Biases integration
- **Hyperparameter Optimization**: Automated tuning capabilities
- **Reproducibility**: Consistent experiment reproduction

</td>
<td>

### 🔬 Clinical & Regulatory Ready

- **FDA Compliance**: Designed for SaMD regulatory requirements
- **Risk Management**: ISO 14971-compliant risk management
- **Clinical Validation**: Protocols for clinical testing
- **Human Factors**: Human-in-the-loop validation

</td>
</tr>
<tr>
<td>

### 🔒 Quality & Security

- **Code Quality**: Black, isort, Flake8, mypy via pre-commit
- **Testing**: Comprehensive unit, integration, and system tests
- **Security Framework**: Threat modeling and secure coding
- **Documentation**: Extensive API and architecture documentation

</td>
<td>

### 🚀 Deployment Ready

- **Real-time Inference**: Online BCI inference capabilities
- **Embedded Systems**: Deployment to exoskeleton hardware
- **Monitoring**: Performance tracking and drift detection
- **OTA Updates**: Safe over-the-air update mechanisms

</td>
</tr>
</table>

## 🏛️ Repository Structure

The project follows a comprehensive structure designed for maintainability, regulatory compliance, and scalability:

```
/chimera_v2.0/
├── src/                      # Core source code
│   └── chimera/              # Main package
│       ├── data/             # Data handling modules
│       ├── processing/       # Signal processing
│       ├── features/         # Feature extraction
│       ├── models/           # ML model implementations
│       ├── training/         # Training logic
│       ├── evaluation/       # Evaluation metrics
│       ├── inference/        # Inference with monitoring
│       ├── deployment/       # Deployment utilities
│       └── utils/            # Shared utilities
├── tests/                    # Automated tests
├── docs/                     # Documentation
├── regulatory/               # Regulatory compliance
├── clinical/                 # Clinical validation
├── quality/                  # Quality management
├── security/                 # Security framework
├── architecture/             # Architecture documentation
├── data/                     # Data with governance
├── models/                   # Model artifacts & documentation
├── notebooks/                # Jupyter notebooks
├── scripts/                  # Runnable scripts
├── config/                   # Configuration files
├── benchmarks/               # Performance benchmarking
├── deployment/               # Deployment pipeline
└── research/                 # Research collaboration
```

## 🚀 Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/) (>=3.9, <3.12)
- [Poetry](https://python-poetry.org/docs/#installation) (>=1.2)
- [DVC](https://dvc.org/doc/install) (>=2.0)
- (Optional) [Make](https://www.gnu.org/software/make/) for using Makefile shortcuts

### Installation & Setup

1. **Clone the Repository**:

```bash
git clone https://github.com/heya-vyom/chimera_v2.0.git
cd chimera_v2.0
```

2. **Install Dependencies**:

```bash
# Install main + all dev dependencies & optional extras in a virtual env
poetry install --all-extras
# Or just core + specific extras: poetry install --extras "torch mlflow"
```

3. **Activate Environment**:

```bash
poetry shell
```

4. **Install Git Hooks (Recommended)**:

```bash
# Ensures linting/formatting checks run before commits
pre-commit install
# Or using Make:
make setup-dev # Also installs dependencies and hooks
```

5. **Fetch Data & Models**:
*(Ensure your DVC remote access is configured)*

```bash
dvc pull data/01_raw # Start with raw data
# Or pull all tracked data/models:
# dvc pull
# Or using Make:
# make dvc-pull
```

### Quick Verification

```bash
make lint # Check if linters run without errors
make test-unit # Run fast unit tests
# Try importing the package
python -c "import chimera; print('Chimera installed successfully!')"
```

## ⚙️ Configuration (Hydra)

Chimera uses [Hydra](https://hydra.cc/) for managing configurations, allowing for flexible experiment setup and reproducibility.

<div align="center">
<img src="https://mermaid.ink/img/pako:eNp1ksFugzAMhl_F8qkV6hvkgNqqE5PW7TDtsFxCcWA0JVHiVFOFePfFQKHVNF8S-_-_2I4PrFCJkMEbsZqUxg_JrUZSLIpPSN5ajeSgHUkR0BmtfUL6qkVAQchrFESKkApwQVp4QyrAWZiGaZiGafgXO99HFeAiTMM0TMM0TMO_2FmAyzAN0zAN0zANY-fnqAJchWmYhmmYhmmYhrHzW1QBrsM0TMM0TMM0TMPY-SOqADdhGqZhGqZhGqZh7PwZVYC7MA3TMA3TMA3TMHZ-jyrAQ5iGaZiGaZiGaRg7H6MK8BimYRqmYRqmYRrGzlNUAZ7CNEzDNEzDNEzD2DmPKsBTmIZpmIZpmIZpGDsXUQV4CtMwDdMwDdMwDWPnMqoAz2EapmEapmEapmHsXEUV4DlMwzRMwzRMwzSMneuoAryEaZiGaZiGaZiGsXMTVYCXMA3TMA3TMA3TMHZuowrwEqZhGqZhGqZhGsbOXVQBXsM0TMM0TMM0TMPYuY8qwGuYhmmYhmmYhmkYOw9RBXgN0zAN0zAN0zANY-cxqgCvYRqmYRqmYRqmYew8RRXgLUzDNEzDNEzDNIyd56gCvIVpmIZpmIZpmIaxcxFVgLcwDdMwDdMwDdMwdi6jCvAepmEapmEapmEaxs5VVAHewzRMwzRMwzRMw9i5jirAe5iGaZiGaZiGaRg7N1EFeA_TMA3TMA3TMA1j5zaqAB9hGqZhGqZhGqZh7NxFFeAjTMM0TMM0TMM0jJ37qAJ8hGmYhmmYhmmYhrHzEFWAjzAN0zAN0zAN0zB2HqMK8BGmYRqmYRqmYRrGzlNUAT7DNEzDNEzDNEzD2HmOKsBnmIZpmIZpmIZpGDsXUQX4DNMwDdMwDdMwDWPnMqoAX2EapmEapmEapmHsXEUV4CtMwzRMwzRMwzSMneuoAvwO0zAN0zAN0zANY-cmqgC_wzRMwzRMwzRMw9i5jSrA7zAN0zAN0zAN0zB27qIK8CdMwzRMwzRMwzSMnfuoAvwJ0zAN0zAN0zANY-chqgB_wjRMwzRMwzRMw9h5jCrAnzAN0zAN0zAN0zB2nqIK8DdMwzRMwzRMwzSMneeoAvwN0zAN0zAN0zANY-ciqgB_wzRMwzRMwzRMw9i5jCrAvzAN0zAN0zAN0zB2rqIK8C9MwzRMwzRMwzSMneuoAvwL0zAN0zAN0zANY-cmqgD_wjRMwzRMwzRMw9i5jSrA_zAN0zAN0zAN0zB27qIK8H-YhmmYhmmYhmkYO_dRBfgfpmEapmEapmEaxs5DVAH-h2mYhmmYhmmYhrHzGFWA_2EapmEapmEapmHsPEUV4CtMwzRMwzRMwzSMnef4D5aTJwA?type=png" alt="Configuration Structure" width="700px" />
</div>

- **Main Config**: `config/main.yaml` acts as the entry point.
- **Composition**: Configurations are composed from subdirectories.
- **Command-Line Overrides**:

```bash
python scripts/train.py model=eeg_cnn_v1 training.epochs=50 +data.subject_id=3
```

## ▶️ Basic Usage (Scripts)

The primary way to run ML tasks is through the scripts in the `/scripts` directory:

1. **Process Raw Data**:

```bash
# Run using default settings in config/data_processing.yaml
python scripts/run_processing.py
    
# Override filter settings for a specific run
python scripts/run_processing.py processing.filter.low_cutoff=0.5 processing.filter.high_cutoff=40.0
```

2. **Train a Model**:

```bash
# Train using the default model and training config
python scripts/train.py
    
# Train a specific model config with a specific training config
python scripts/train.py model=eeg_cnn_v1 training=experiment_01
    
# Train for a specific subject, overriding learning rate
python scripts/train.py +data.subject_id=5 training.optimizer.lr=0.0001
```

3. **Evaluate a Model**:

```bash
# Evaluate a model saved locally (tracked by DVC)
python scripts/evaluate.py model.checkpoint_path=models/classifiers/eeg_cnn_v1_final.h5 data.fold=test
    
# Evaluate a model from an MLflow run
python scripts/evaluate.py +experiment.tracking_uri=http://localhost:5000 +experiment.run_id=YOUR_MLFLOW_RUN_ID
```

4. **Run Batch Inference**:

```bash
python scripts/batch_inference.py model.checkpoint_path=models/classifiers/lda_subject001.pkl inference.input_path=data/04_model_input/new_session_features.npz inference.output_path=predictions/new_session_preds.csv
```

### Makefile Shortcuts

For convenience, common commands are available via `make`:

```bash
make help            # Show available commands
make lint            # Run all linters
make format          # Apply code formatting
make test            # Run all tests
make test-cov        # Run tests with coverage report
make clean           # Remove temporary files/caches
make requirements    # Generate requirements.txt from pyproject.toml
```

## 🧪 Testing

Chimera includes a comprehensive testing suite:

```bash
# Run all tests
pytest
# Or: make test

# Run only unit tests
pytest tests/unit
# Or: make test-unit

# Run tests and generate a coverage report
pytest --cov=src/chimera --cov-report=term-missing
# Or: make test-cov
```

## 🔬 Regulatory Compliance

Chimera is designed with regulatory compliance in mind, following FDA guidelines for Software as a Medical Device (SaMD) with AI/ML components.

<div align="center">
<img src="https://mermaid.ink/img/pako:eNp1kk9PwzAMxb9KlBOI9QvkMG3qBBJiB8QOvUQmMY3WJlWSMjZV_e7YbVlhwJf4-fez_OzCuJUEBbwQb8lYvGvDLZIVUXxA8t5ZJA_WkVYRXdA6JGQvVkWUhLxGRWQMqQhXZJV3pCNcxHmcx1mcx_9i5_uoI1zGeZzHeZzH-b_YRYRXcR7ncR7ncR7nMXZ-jjrCdZzHeZzHeZzHeYyd36KO8C7O4zzO4zzO4zzGzh9RR_gY53Ee53Ee53EeY-fPqCP8ivM4j_M4j_M4j7HzLuoIf-I8zuM8zuM8zmPs_Bt1hMc4j_M4j_M4j_MYO0-ijvAU53Ee53Ee53EeY-c0wlOcx3mcx3mcx3mMnbMIT3Ee53Ee53Ee5zF2ziM8xXmcx3mcx3mcx9i5iPAU53Ee53Ee53EeY-cywnOcx3mcx3mcx3mMnasIz3Ee53Ee53Ee5zF2riO8xHmcx3mcx3mcx9i5ifAS53Ee53Ee53EeY-c2wkucx3mcx3mcx3mMnbsIL3Ee53Ee53Ee5zF27iO8xnmcx3mcx3mcx9h5iPAa53Ee53Ee53EeY-cxwmucx3mcx3mcx3mMnacIb3Ee53Ee53Ee5zF2niO8xXmcx3mcx3mcx9h5ifAW53Ee53Ee53EeY-c1wlucx3mcx3mcx3mMnbcI73Ee53Ee53Ee5zF23iO8x3mcx3mcx3mcx9j5iPAe53Ee53Ee53EeY-czwnucx3mcx3mcx3mMna8IH3Ee53Ee53Ee5zF2viN8xHmcx3mcx3mcx9j5ifAR53Ee53Ee53EeY-e_CB9xHudxHudxHucxdv4HxvXwKQ?type=png" alt="Regulatory Framework" width="700px" />
</div>

Key regulatory components:

- **FDA Strategy**: Documentation of regulatory pathway in `regulatory/fda_strategy.md`
- **Risk Management**: ISO 14971-compliant risk management in `regulatory/risk_management/`
- **Quality Management**: Lightweight QMS appropriate for the current stage in `quality/`
- **Clinical Validation**: Framework for clinical testing in `clinical/`

## 🔒 Security Framework

Chimera includes a comprehensive security framework:

- **Security Policy**: Overall security approach in `security/security_policy.md`
- **Threat Models**: Systematic threat analysis in `security/threat_models/`
- **Security Testing**: Procedures for security validation in `security/security_testing/`
- **Secure Coding Guidelines**: Best practices in `security/secure_coding_guidelines.md`

## 📊 Data Governance

Data governance is a critical component of Chimera:

- **Data Quality Metrics**: Definitions and thresholds in `data/governance/data_quality_metrics.md`
- **Data Dictionary**: Comprehensive data dictionary in `data/governance/data_dictionary.md`
- **Provenance Tracking**: Implementation in `data/governance/provenance_tracking.py`
- **Bias Detection**: Tools in `data/governance/bias_detection.py`

## 🧠 Model Documentation

Chimera includes comprehensive model documentation:

- **Model Cards**: Google-style model cards in `models/documentation/model_cards/`
- **Performance Reports**: Analysis reports in `models/documentation/performance_reports/`
- **Limitations**: Known limitations in `models/documentation/limitations.md`

## 🛣️ Roadmap

<div align="center">
<img src="https://mermaid.ink/img/pako:eNp1kk9PwzAMxb9KlBOI9QvkMG3qBBJiB8QOvUQmMY3WJlWSMjZV_e7YbVlhwJf4-fez_OzCuJUEBbwQb8lYvGvDLZIVUXxA8t5ZJA_WkVYRXdA6JGQvVkWUhLxGRWQMqQhXZJV3pCNcxHmcx1mcx_9i5_uoI1zGeZzHeZzH-b_YRYRXcR7ncR7ncR7nMXZ-jjrCdZzHeZzHeZzHeYyd36KO8C7O4zzO4zzO4zzGzh9RR_gY53Ee53Ee53EeY-fPqCP8ivM4j_M4j_M4j7HzLuoIf-I8zuM8zuM8zmPs_Bt1hMc4j_M4j_M4j_MYO0-ijvAU53Ee53Ee53EeY-c0wlOcx3mcx3mcx3mMnbMIT3Ee53Ee53Ee5zF2ziM8xXmcx3mcx3mcx9i5iPAU53Ee53Ee53EeY-cywnOcx3mcx3mcx3mMnasIz3Ee53Ee53Ee5zF2riO8xHmcx3mcx3mcx9i5ifAS53Ee53Ee53EeY-c2wkucx3mcx3mcx3mMnbsIL3Ee53Ee53Ee5zF27iO8xnmcx3mcx3mcx9h5iPAa53Ee53Ee53EeY-cxwmucx3mcx3mcx3mMnacIb3Ee53Ee53Ee5zF2niO8xXmcx3mcx3mcx9h5ifAW53Ee53Ee53EeY-c1wlucx3mcx3mcx3mMnbcI73Ee53Ee53Ee5zF23iO8x3mcx3mcx3mcx9j5iPAe53Ee53Ee53EeY-czwnucx3mcx3mcx3mMna8IH3Ee53Ee53Ee5zF2viN8xHmcx3mcx3mcx9j5ifAR53Ee53Ee53EeY-e_CB9xHudxHudxHucxdv4HxvXwKQ?type=png" alt="Project Roadmap" width="700px" />
</div>

- [x] Core ML pipeline implementation
- [x] Regulatory compliance framework
- [ ] Advanced spatial filtering techniques
- [ ] Online adaptation algorithms
- [ ] Robust cross-subject generalization models
- [ ] Deployment pipeline for embedded systems / ROS
- [ ] Expanded documentation with detailed tutorials

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:

- Setting up your development environment
- Reporting bugs and suggesting features
- Coding standards (PEP 8, Black, Flake8, isort, mypy)
- Testing requirements
- Pull Request process

All participants are expected to adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## 📜 License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## ✉️ Contact

- **Technical Lead:** Vyom (vyommallick@gmail.com)
- **Bug Reports / Feature Requests:** [GitHub Issues](https://github.com/heya-vyom/chimera_v2.0/.github/ISSUE_TEMPLATE)

---

<div align="center">
<p>
<strong>Chimera: Restoring Movement Through the Power of Thought</strong><br>
Open Source | FDA Compliance Ready | Research Driven
</p>
</div>
