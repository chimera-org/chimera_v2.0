# 🧠 Chimera ML Operational Playbook 🚀

Welcome, Engineer, to the Chimera ML Operational Playbook! This is your definitive guide to navigating and leveraging the `chimera_v2.0` repository for cutting-edge BCI research and development. Consider this the operational manual for our mission to restore movement.

This document assumes you've completed the initial onboarding: environment setup via [README.md](https://github.com/heya-vyom/chimera_v2.0/README.md) and familiarization with contribution protocols in [CONTRIBUTING.md](https://github.com/heya-vyom/chimera_v2.0/CONTRIBUTING.md).

**🎯 Objective:** To provide a comprehensive, best-practice-driven guide for executing core machine learning workflows – from data ingestion to model deployment readiness – within the Chimera ecosystem.

## 📜 Table of Contents

1. ✅ Prerequisites Checklist (#prerequisites-checklist)

2. ⚙️ Mastering Configuration (Hydra) (#mastering-configuration-hydra)

    - The Philosophy: Config-Driven Execution (#the-philosophy-config-driven-execution)

    - Structure & Composition Deep Dive (#structure--composition-deep-dive)

    - Power-User: Command-Line Overrides (#power-user-command-line-overrides)

    - Accelerating Experiments: Multi-Run Execution (#accelerating-experiments-multi-run-execution)

3. 🌊 Workflow: The Data Pipeline (#workflow-the-data-pipeline)

    - Ingesting Raw Signals (The Source) (#ingesting-raw-signals-the-source)

    - Executing Processing & Feature Extraction (#executing-processing--feature-extraction)

    - Data Integrity: Versioning with DVC (#data-integrity-versioning-with-dvc)

4. 🏋️ Workflow: Model Training & Experimentation (#workflow-model-training--experimentation)

    - Launching a Training Mission () (#launching-a-training-mission-scriptstrainpy)

    - Strategic Selection: Models & Training Regimes (#strategic-selection-models--training-regimes)

    - Observability: Experiment Tracking (MLflow/W&B) (#observability-experiment-tracking-mlflowwb)

    - Artifact Management: Versioning Trained Models (#artifact-management-versioning-trained-models)

5. 📊 Workflow: Rigorous Model Evaluation (#workflow-rigorous-model-evaluation)

    - Evaluating Checkpointed Models (#evaluating-checkpointed-models)

    - Evaluating via Experiment Tracker Runs (#evaluating-via-experiment-tracker-runs)

6. 💡 Workflow: Inference Engine (#workflow-inference-engine)

    - Batch Predictions: Offline Analysis (#batch-predictions-offline-analysis)

    - Real-Time Ready: Online Inference Considerations (#real-time-ready-online-inference-considerations)

7. 🧪 Advanced Ops: Hyperparameter Optimization (#advanced-ops-hyperparameter-optimization)

8. 💾 Version Control Synergy (Git + DVC) (#version-control-synergy-git--dvc)

    - The Protocol: Tracking New Artifacts (#the-protocol-tracking-new-artifacts)

    - Time Travel: Switching Data/Model States (#time-travel-switching-datamodel-states)

9. 🌱 Environment Management Mastery (Poetry) (#environment-management-mastery-poetry)

10. ✨ Developer Workflow: Adding New Capabilities (Checklist) (#developer-workflow-adding-new-capabilities-checklist)

11. 🩺 Debugging & Troubleshooting Toolkit (#debugging--troubleshooting-toolkit)

12. 💡 Guiding Principles & Best Practices (#guiding-principles--best-practices)

13. ❓ Getting Support (#getting-support)

---

## 1. ✅ Prerequisites Checklist

Confirm you've completed the foundational setup before diving into workflows:

- [x] Repository cloned (`git clone ...`).

- [x] Dependencies installed via Poetry (`poetry install --all-extras`).

- [x] Poetry virtual environment activated (`poetry shell`).

- [x] Pre-commit hooks installed (`pre-commit install`).

- [x] DVC remote storage access configured (`dvc remote list` shows correct remote).

- [x] Essential baseline data pulled (`dvc pull data/01_raw` or similar).

---

## 2. ⚙️ Mastering Configuration (Hydra)

Hydra is the central nervous system for configuring experiments and pipelines in `chimera_v2.0`. Understanding it is non-negotiable for efficient R&D.

### The Philosophy: Config-Driven Execution

- **Separation of Concerns:** Code (`src/`) defines *how* tasks are done; Config (`config/`) defines *what* parameters are used. This enables reproducibility and rapid experimentation without code changes.

- **Reproducibility:** Each run's exact configuration is snapshotted by Hydra (in `outputs/`), ensuring you can always recreate results.

### Structure & Composition Deep Dive

- **Location:** All YAML configs live in `/config`.

- **Entry Point:** `config/main.yaml` usually sets the default combination of components.

- **Composition (**`defaults` **list):** This list within a YAML file dictates which other config files are loaded. It enables modularity. Example from `config/main.yaml`:

    ```yaml
    # config/main.yaml (Example)
    defaults:
      # Load default configurations for each stage/component
      - data_processing: default
      - features: default
      # Select a specific model configuration to use by default
      - model: eeg_cnn_v1
      - training: default
      # Use custom logging configurations provided by Hydra plugins
      - override hydra/job_logging: colorlog
      - override hydra/hydra_logging: colorlog
    
    # Global parameters shared across runs unless overridden
    project_name: "chimera_ml"
    seed: 42 # For reproducibility!
    ```

- **Config Groups:** Directories like `config/model/` or `config/training/` act as namespaces. You can have multiple options within each (e.g., `model/eeg_cnn_v1.yaml`, `model/lda_basic.yaml`).

### Power-User: Command-Line Overrides

Modify behavior *without touching config files*:

- **Tune Parameters:**

    ```bash
    # Adjust learning rate for this specific run
    python scripts/train.py training.optimizer.lr=0.0001 model.dropout_rate=0.3
    ```

- **Swap Components:**

    ```bash
    # Use the LDA model config instead of the default CNN
    python scripts/train.py model=lda_subject_calibrated
    ```

- **Add New Parameters:** (Useful for run-specific tags or identifiers)

    ```bash
    python scripts/train.py +experiment_tag=subject_5_retrain
    ```

- **Syntax:** `~` for null/None, `\` to escape special chars, `+` to add keys not in the original config. Consult the [Hydra Docs](https://hydra.cc/docs/intro/).

### Accelerating Experiments: Multi-Run Execution

Hydra's `--multirun` flag is your accelerator for exploring parameter spaces:

```bash
# Sweep over learning rates and dropout values simultaneously
python scripts/train.py --multirun \
    model=eeg_cnn_v1 \
    training.optimizer.lr=0.01,0.001,0.0001 \
    model.dropout_rate=0.25,0.5
```



This launches multiple independent runs, each with a different parameter combination, saving significant manual effort. Essential for HPO (see Section 7).

---

## 3. 🌊 Workflow: The Data Pipeline

Transforming raw brain signals into model-ready features follows a structured pipeline, managed by scripts and versioned by DVC.

### Ingesting Raw Signals (The Source)

- **Standard Location:** Place raw data files (EDF, BDF, etc.) meticulously into data/01_raw/, adhering to the subject_XXX/session_YYY/ structure. This raw data is considered **immutable**.

- **Fetching:** Use scripts/ingest_data.py (if it exists for your data source) or follow documented manual procedures.

- **Versioning (Critical!):** Immediately version new raw data with DVC:

    ```text
    # 1. Stage the new data directory with DVC
    dvc add data/01_raw/subject_005
    # 2. Stage the generated .dvc file and .gitignore changes with Git
    git add data/01_raw/subject_005.dvc data/01_raw/.gitignore
    # 3. Commit the change pointer in Git
    git commit -m "feat(data): Ingest raw data for subject 005"
    # 4. Upload the actual data files to DVC remote storage
    dvc push data/01_raw/subject_005.dvc
    ```



### Executing Processing & Feature Extraction

- **The Engine:** scripts/run_processing.py (or similar) drives this stage. It loads configurations from config/data_processing.yaml and config/features.yaml (as selected via main.yaml or overrides).

- **Execution:**

    ```text
    # Run using the composed default configurations
    python scripts/run_processing.py
    # Run targeting specific subjects with a custom filter config
    python scripts/run_processing.py data_processing=custom_filter +subject_ids=[1, 2, 7]
    ```

- **Outputs:** Generates intermediate files in data/02_processed/, features in data/03_features/, and final model inputs in data/04_model_input/ (paths are configurable).

- **Monitoring:** Pay attention to console logs. Detailed logs and the exact config snapshot are stored in the Hydra output directory (e.g., outputs/YYYY-MM-DD/HH-MM-SS/).

### Data Integrity: Versioning with DVC

Intermediate and final processed data should also be versioned to ensure experiments using them are reproducible.

```text
# After generating new features/model inputs successfully
dvc add data/03_features/ data/04_model_input/
git add data/03_features.dvc data/04_model_input.dvc data/.gitignore
git commit -m "chore(data): Generate features v2 using updated processing pipeline"
dvc push data/03_features.dvc data/04_model_input.dvc
```

---

## 4. 🏋️ Workflow: Model Training & Experimentation

The core loop of training models, tracking progress, and managing artifacts.

### Launching a Training Mission (scripts/train.py)

This script orchestrates the training process defined in src/chimera_ml/training/.

```text
# Train with default settings defined in config/main.yaml
python scripts/train.py
# Train a specific model configuration for more epochs
python scripts/train.py model=eeg_cnn_v1_large training.epochs=200
```

- **Inputs:** Consumes data from data/04_model_input/.

- **Outputs:**

    - Real-time logging to console.

    - Metrics, parameters, and potentially artifacts logged to MLflow/WandB.

    - Model checkpoints saved periodically or at the end (location configured).

    - Hydra output directory (outputs/...) with logs and config snapshot.

### Strategic Selection: Models & Training Regimes

Leverage Hydra overrides to precisely control your experiments:

```text
# Compare LDA vs CNN using the same 'standard' training config
python scripts/train.py --multirun model=lda_basic,eeg_cnn_v1 training=standard
# Test a different optimizer defined in config/training/optimizer/adamw.yaml
python scripts/train.py training/optimizer=adamw
```

### Observability: Experiment Tracking (MLflow/W&B)

- **Integration:** Core training logic (src/training/trainer.py) should automatically log key information (hyperparameters, metrics per epoch, final results, potentially model artifacts) to your configured tracker.

- **Setup:** Ensure MLFLOW_TRACKING_URI is set or you're logged into WandB (wandb login).

- **Analysis:** Use the MLflow UI (mlflow ui) or WandB dashboard to visualize learning curves, compare runs, analyze hyperparameters, and inspect saved artifacts. This is crucial for understanding model behavior.

### Artifact Management: Versioning Trained Models

How you version depends on whether you primarily use the tracker or DVC:

- **Tracker-Based (MLflow/WandB Preferred):**

    - Configure training script to log the final model artifact directly to the tracker.

    - Retrieve models using the Run ID provided by the tracker. This keeps models tightly coupled with their experimental results.

- **DVC-Based:**

    - Configure training script to save models to a specific path within /models.

    - Use the standard dvc add/git add/git commit/dvc push workflow:

        ```text
        dvc add models/classifiers/cnn_final_subj_007.h5
        git add models/classifiers/cnn_final_subj_007.h5.dvc models/.gitignore
        git commit -m "feat(model): Add trained CNN model for subject 007, run XYZ"
        dvc push models/classifiers/cnn_final_subj_007.h5.dvc
        ```

---

## 5. 📊 Workflow: Rigorous Model Evaluation

Objectively measuring model performance on unseen data.

### Evaluating Checkpointed Models

Use scripts/evaluate.py with models stored locally (tracked via DVC or simple checkpoints).

```text
# Evaluate a DVC-tracked model on the default test set
python scripts/evaluate.py model.checkpoint_path=models/classifiers/best_lda_model.pkl
# Evaluate on validation split for a specific subject
python scripts/evaluate.py model.checkpoint_path=outputs/SOME_RUN/checkpoints/epoch_10.ckpt +data.split=validation +data.subject_id=3
```

- **Inputs:** Path to the model file, configuration specifying the evaluation dataset (data.split, data.subject_id, etc.).

- **Outputs:** Prints key metrics (Accuracy, F1, Kappa, Confusion Matrix, custom BCI metrics). May save detailed results/plots.

### Evaluating via Experiment Tracker Runs

Leverage the tracker to evaluate models logged during training.

```text
# Evaluate model from MLflow run ID (ensure tracker URI is accessible)
python scripts/evaluate.py +experiment.run_id=YOUR_MLFLOW_RUN_ID data.split=test
# Evaluate model from WandB run path
python scripts/evaluate.py +experiment.wandb_run_path="YourOrg/YourProject/RUN_ID" data.split=test
```

Note: scripts/evaluate.py needs the logic to fetch the model artifact based on the provided run ID/path.

---

## 6. 💡 Workflow: Inference Engine

Applying trained models to generate predictions.

### Batch Predictions: Offline Analysis

Use scripts/batch_inference.py for generating predictions on a static dataset.

```text
# Predict on new feature file using a specific model
python scripts/batch_inference.py \
    model.checkpoint_path=models/classifiers/production_model_v1.pkl \
    inference.input_feature_path=data/03_features/new_session_subject_009.npz \
    inference.output_prediction_path=predictions/subject_009_preds.csv
```

### Real-Time Ready: Online Inference Considerations

- **Core Logic:** Resides in src/chimera_ml/inference/online.py and potentially src/deployment/.

- **Pipeline:** Involves loading the model (predictor.py), buffering incoming data segments, applying exactly the same preprocessing/feature extraction used during training (critical!), predicting, and mapping outputs to commands (control_mapper.py).

- **Execution:** The actual real-time system likely runs via separate scripts or integration layers (e.g., ROS nodes, dedicated C++ application) that import and use the functions and classes defined within src/chimera_ml. Consult docs/deployment.md.

---

## 7. 🧪 Advanced Ops: Hyperparameter Optimization

Systematically find optimal model parameters using Hydra's sweepers (e.g., Optuna).

- **Trigger Script:** Often scripts/train.py itself, activated by --multirun and Hydra sweeper configs, or a dedicated scripts/tune_hyperparameters.py.

- **Configuration:** Define search spaces using Optuna's syntax directly within your YAML configs (e.g., config/training/tuning_setup.yaml).

- **Example Launch:**

    ```text
    python scripts/train.py --multirun \
        hydra/sweeper=optuna \
        hydra.sweeper.direction=maximize \
        hydra.sweeper.study_name=cnn_arch_tuning \
        hydra.sweeper.n_trials=100 \
        'hydra.sweeper.search_space={ \
          "training.optimizer.lr": {"type": "float", "low": 1e-5, "high": 1e-2, "log": true}, \
          "model.num_filters": {"type": "int", "low": 8, "high": 64, "step": 8}, \
          "model.dropout_rate": {"type": "float", "low": 0.1, "high": 0.6} \
        }' \
        # Add other fixed model/training parameters here
        model=eeg_cnn_base training=default
    ```

- **Analysis:** Use the experiment tracker (MLflow/WandB) or Optuna's visualization tools to find the best trial and corresponding hyperparameters.

---

## 8. 💾 Version Control Synergy (Git + DVC)

Git versions your code and configurations. DVC versions your large data and model files. They work together.

### The Protocol: Tracking New Artifacts

- dvc add <path/to/data_or_model>: Tells DVC to track the file/directory. Creates/updates a .dvc file.

- git add <path/to/data_or_model.dvc> .gitignore: Stages the pointer (.dvc file) and any .gitignore updates in Git.

- git commit -m "...": Records the pointer's version in Git history.

- dvc push <path/to/data_or_model.dvc>: Uploads the actual large file(s) to DVC remote storage.

### Time Travel: Switching Data/Model States

- git checkout <branch_or_commit>: Switches your code and .dvc file pointers to a specific version.

- dvc checkout: Downloads/links the data and model files corresponding to the .dvc files currently checked out in Git. Your /data and /models directories will update to match the state of that commit.

---

## 9. 🌱 Environment Management Mastery (Poetry)

Poetry ensures everyone uses the exact same dependencies.

- **Activate:** Always work within the activated environment: poetry shell.

- **Install:** Use poetry install (with optional --extras or --no-dev).

- **Add Dependency:** poetry add <package_name> (for main deps) or poetry add --group dev <package_name> (for dev tools). This updates pyproject.toml and poetry.lock. Commit these files!

- **Update:** poetry update <package_name> (to update one) or poetry update (to update all according to pyproject.toml constraints).

- **Inspect:** poetry show (list all packages), poetry show <package_name> (details of one).

- **Reproducibility:** The poetry.lock file guarantees that poetry install always installs the exact same versions of all dependencies, crucial for avoiding "works on my machine" issues.

---

## 10. ✨ Developer Workflow: Adding New Capabilities (Checklist)

Follow these steps when contributing new features or fixes:

- **Branch:** Create a descriptive branch from main (git checkout -b feature/my-new-thing).

- **Core Logic (src/):** Implement reusable code in the appropriate chimera_ml module. Adhere to existing design patterns.

- **Configuration (config/):** Add/update YAML files if new parameters are needed. Keep it structured.

- **Tests (tests/):** Write comprehensive unit (and integration, if needed) tests using pytest. Aim for high coverage. Test edge cases!

- **Scripts (scripts/):** Update or add scripts if needed to expose the new functionality via the command line, leveraging the core logic.

- **Docstrings:** Add clear Google-style docstrings to all new public functions/classes/methods.

- **Documentation (docs/):** Update this guide, architecture docs, or other relevant markdown files.

- **Checks Pass:** Run make lint and make test locally and fix all issues.

- **Commit:** Use conventional commit messages (git commit). Pre-commit hooks will run.

- **Pull Request:** Push your branch and open a PR using the template. Ensure CI checks pass on GitHub. Engage in code review.

---

## 11. 🩺 Debugging & Troubleshooting Toolkit

When things go wrong:

- **Hydra Outputs:** The outputs/YYYY-MM-DD/HH-MM-SS/ directory is your first stop. Check .hydra/config.yaml (what actually ran) and the .log file.

- **Logging:** Add more detailed logging (import logging; log = logging.getLogger(__name__); log.debug(...)) in src/. Control verbosity via Hydra's logging config.

- **Debugger (pdb/ipdb):** Insert import ipdb; ipdb.set_trace() or import pdb; pdb.set_trace() in your code to enter an interactive debugging session.

- **Isolate & Inspect:**

    - Test functions/classes individually using pytest.

    - Load intermediate data (dvc checkout data/02_processed/..., then load in a notebook) to inspect pipeline stages.

- **Environment Check:** Run poetry check and poetry show to look for dependency issues. Ensure you're in the poetry shell.

- **Common Errors:** See [Troubleshooting & FAQ](https://www.google.com/url?sa=E&q=%23troubleshooting--faq) below.

---

## 12. 💡 Guiding Principles & Best Practices

- **Configuration over Code:** Parameterize everything possible via Hydra configs.

- **Version Everything:** Code (Git), Data/Models (DVC), Environment (poetry.lock).

- **Test Rigorously:** Write tests before or during development, not just after. Cover edge cases.

- **Automate:** Use pre-commit hooks and CI/CD (GitHub Actions) for quality checks, testing, and potentially deployment steps.

- **Modularity:** Keep components in src/ focused and reusable. Scripts orchestrate, src/ implements.

- **Track Experiments:** Use MLflow/WandB diligently. Your future self will thank you.

- **Small, Focused PRs:** Easier to review, less likely to introduce bugs.

- **Document Decisions:** Use docstrings, comments, commit messages, and /docs to explain the why.

---

## 13. ❓ Getting Support

If you're stuck after consulting this guide, project docs, and searching issues:

- **GitHub Issues:** Check the [Issue Tracker][Link to Issue Tracker] first. If your problem isn't there, open a new, detailed issue (use templates!).

- **Team Channel:** Ask on [Specify #chimera-ml Slack Channel or relevant communication method]. Provide context, what you've tried, and relevant logs/configs.

---

This Playbook is a dynamic resource. Contribute improvements via PRs!

Link to Issue Tracker: [Issue Tracker](https://github.com/heya-vyom/chimera_v2.0/ISSUE_TRACKER.md)

