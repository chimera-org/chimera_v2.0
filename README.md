# Chimera 🧠: Machine Learning for Mind-Controlled Exoskeletons

[![Build Status](https://img.shields.io/github/actions/workflow/status/heya-vyom/chimera_v2.0/tests.yml?branch=main&style=flat-square)](https://github.com/heya-vyom/chimera_v2.0/actions/workflows/tests.yml) <!-- Update with actual CI badge link -->
[![Code Coverage](https://img.shields.io/codecov/c/github/[Your%20Org%20or%20Username]/chimera-ml?style=flat-square)](https://codecov.io/gh/[Your%20Org%20or%20Username]/chimera-ml) <!-- Update with actual Coverage badge link -->
[![License](https://img.shields.io/github/license/[Your%20Org%20or%20Username]/chimera-ml?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue?style=flat-square)](pyproject.toml) <!-- Verify supported versions -->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square)](https://github.com/pre-commit/pre-commit)
[![Documentation Status](https://img.shields.io/readthedocs/[your-docs-project-name]?style=flat-square)](https://[your-docs-project-name].readthedocs.io/en/latest/) <!-- Update if using ReadTheDocs or similar -->

Core Machine Learning engine for the **Chimera Project**. This repository focuses on processing Electroencephalography (EEG) signals to decode movement intentions for controlling a robotic exoskeleton, aiming to restore limb movement for individuals with quadriplegia.

It encompasses the entire ML pipeline from raw data ingestion and preprocessing to model training, evaluation, and deployment-ready inference logic.

## ✨ Features

*   **End-to-End EEG Pipeline:** Modules for data loading, robust signal processing (filtering, artifact removal), feature extraction (CSP, PSD, etc.), and dataset creation.
*   **Flexible Modeling:** Supports classical ML (LDA, SVM) and Deep Learning (EEGNet, ShallowConvNet, custom PyTorch/TensorFlow models) approaches.
*   **Configuration Driven:** Powered by [Hydra](https://hydra.cc/) for easy management of complex configurations (data processing parameters, model hyperparameters, training settings).
*   **Reproducibility Focused:**
    *   [Poetry](https://python-poetry.org/) for precise dependency management.
    *   [DVC](https://dvc.org/) for versioning large data files and models alongside Git.
    *   [MLflow](https://mlflow.org/) / [Weights & Biases](https://wandb.ai/) integration (configurable) for experiment tracking.
*   **Real-time Ready:** Includes components designed for online BCI inference loops (`inference/online.py`).
*   **Quality Assured:** Enforced code style (Black, isort), linting (Flake8), type checking (mypy via pre-commit), and a comprehensive test suite (`pytest`).
*   **Modular & Extensible:** Built as an installable Python package (`chimera_ml`) with clearly defined components.

## 🏛️ Repository Structure

The project adheres to a standard layout for maintainability and scalability:

```plaintext
/chimera-ml/
├── .dvc/             # DVC metadata (data/model versioning)
├── .git/             # Git metadata
├── .github/          # GitHub Actions workflows, issue/PR templates
├── .flake8           # Flake8 linter config
├── .gitignore        # Files ignored by Git
├── .dvcignore        # Files ignored by DVC
├── .pre-commit-config.yaml # pre-commit hook definitions
├── CODE_OF_CONDUCT.md # Community guidelines
├── CONTRIBUTING.md   # Guidelines for contributors
├── LICENSE           # Project License (Apache 2.0)
├── Makefile          # Convenience commands (make test, make lint, ...)
├── README.md         # This overview file
├── pyproject.toml    # Project definition, dependencies (Poetry)
├── requirements.txt  # Pinned dependencies (generated)
│
├── config/           # Configuration files (Hydra/YAML)
│   ├── main.yaml
│   ├── data_processing.yaml
│   ├── features.yaml
│   ├── model/
│   └── training/
│
├── data/             # --> Raw, Processed, Feature data (Tracked by DVC, NOT Git) <--
│   ├── 01_raw/
│   ├── 02_processed/
│   ├── 03_features/
│   └── 04_model_input/
│
├── docs/             # Project documentation (Sphinx/MkDocs source)
│   ├── index.md
│   ├── architecture.md
│   └── ...
│
├── models/           # --> Trained model artifacts (Tracked by DVC/MLflow, NOT Git) <--
│   ├── classifiers/
│   └── signal_processing/
│
├── notebooks/        # Jupyter notebooks for exploration & analysis
│
├── scripts/          # Runnable scripts for core ML tasks
│   ├── ingest_data.py
│   ├── run_processing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── batch_inference.py
│   └── tune_hyperparameters.py
│
├── src/              # Core source code (installable package)
│   └── chimera_ml/
│       ├── __init__.py
│       ├── data/
│       ├── processing/
│       ├── features/
│       ├── models/
│       ├── training/
│       ├── evaluation/
│       ├── inference/
│       ├── deployment/
│       └── utils/
│
└── tests/            # Automated tests (pytest)
    ├── conftest.py
    ├── unit/
    ├── integration/
    └── system/
```

## 🚀 Getting Started

### Prerequisites

- [Git](https://git-scm.com/)

- [Python](https://www.python.org/downloads/) (>=3.9, <3.12 - see `pyproject.toml`)

- [Poetry](https://python-poetry.org/docs/#installation) (`>=1.2`)

- [DVC](https://dvc.org/doc/install) (`>=2.0`)

- (Optional but Recommended) [Make](https://www.gnu.org/software/make/) for using Makefile shortcuts.

- Access to the DVC remote storage (e.g., S3 bucket, SSH server) where data/models are stored.

### Installation & Setup

1. **Clone:**

    ```bash
    git clone https://github.com/[Your Org or Username]/chimera-ml.git
    cd chimera-ml
    ```

2. **Install Dependencies:**

    ```bash
    # Installs main + all dev dependencies & optional extras in a virtual env
    poetry install --all-extras
    # Or just core + specific extras: poetry install --extras "torch mlflow"
    ```

3. **Activate Environment:**

    ```bash
    poetry shell
    ```

4. **Install Git Hooks (Recommended):**

    ```bash
    # Ensures linting/formatting checks run before commits
    pre-commit install
    # Or using Make:
    make setup-dev # Also installs dependencies and hooks
    ```

5. **Fetch Data & Models:**
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
python -c "import chimera_ml; print('Chimera ML installed successfully!')"
```

## ⚙️ Configuration (Hydra)

Project parameters are managed via YAML files in the `config/` directory using [Hydra](https://hydra.cc/).

- **Main Config:** `config/main.yaml` often acts as the entry point.

- **Composition:** It typically composes configurations from subdirectories (`data_processing.yaml`, `model/eeg_cnn_v1.yaml`, etc.).

- **Command-Line Overrides:** Easily change parameters for specific runs:

    ```bash
    python scripts/train.py model=lda_subject_calibrated training.epochs=50 +data.subject_id=3
    ```

    Refer to the Hydra documentation for advanced usage like multirun.

## ▶️ Basic Usage (Scripts)

The primary way to run ML tasks is through the scripts in the `/scripts` directory. They use the configurations from `/config`.

*(Ensure the Poetry virtual environment is active:* `poetry shell`*)*

1. **Process Raw Data:**

    ```bash
    # Run using default settings in config/data_processing.yaml
    python scripts/run_processing.py
    
    # Override filter settings for a specific run
    python scripts/run_processing.py processing.filter.low_cutoff=0.5 processing.filter.high_cutoff=40.0
    ```

    *Generates files in* `data/02_processed`*,* `data/03_features`*, etc.*

2. **Train a Model:**

    ```bash
    # Train using the default model and training config specified in main.yaml
    python scripts/train.py
    
    # Train a specific model config with a specific training config
    python scripts/train.py model=eeg_cnn_v1 training=experiment_01
    
    # Train for a specific subject, overriding learning rate
    python scripts/train.py +data.subject_id=5 training.optimizer.lr=0.0001
    ```

    *Outputs logs, saves model artifacts (via DVC or MLflow/WandB), tracks metrics.*

3. **Evaluate a Model:**

    ```bash
    # Evaluate a model saved locally (tracked by DVC)
    python scripts/evaluate.py model.checkpoint_path=models/classifiers/eeg_cnn_v1_final.h5 data.fold=test
    
    # Evaluate a model from an MLflow run
    python scripts/evaluate.py +experiment.tracking_uri=http://localhost:5000 +experiment.run_id=YOUR_MLFLOW_RUN_ID
    ```

    *Prints evaluation metrics.*

4. **Run Batch Inference:**

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
# ... see Makefile for more
```

## 🧪 Testing

Tests are crucial for reliability. We use `pytest`.

```bash
# Run all tests (unit, integration)
pytest
# Or: make test

# Run only unit tests
pytest tests/unit
# Or: make test-unit

# Run tests and generate a coverage report
pytest --cov=src/chimera_ml --cov-report=term-missing
# Or: make test-cov
# View HTML report: open htmlcov/index.html
```

## 🤝 Contributing

We welcome contributions! Please see CONTRIBUTING.md (CONTRIBUTING.md) for detailed guidelines on:

- Setting up your development environment

- Reporting bugs and suggesting features ([Issue Tracker][Link to Issue Tracker])

- Coding standards (PEP 8, Black, Flake8, isort, mypy)

- Testing requirements

- Pull Request process

All participants are expected to adhere to our CODE_OF_CONDUCT.md (CODE_OF_CONDUCT.md).

## 📜 License

This project is licensed under the Apache License, Version 2.0. See the LICENSE (LICENSE) file for details.

## 🛣️ Roadmap (Example)

- [ ] Integrate advanced spatial filtering techniques.

- [ ] Implement online adaptation algorithms.

- [ ] Develop robust cross-subject generalization models.

- [ ] Formalize deployment pipeline for embedded systems / ROS.

- [ ] Expand documentation with detailed tutorials.

## ✉️ Contact

- **Technical Lead:** `[Vyom / vyommallick@gmail.com]`

- **Bug Reports / Feature Requests:** [GitHub Issues](ISSUE_TRACKER.md)

- **General Discussion:** `[Slack Channel / Mailing List, if applicable]`

---

*[Link to Issue Tracker]:* [https://github.com/heya-vyom/chimera_v2.0/ISSUE_TRACKER.md]
