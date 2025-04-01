# Contributing to Chimera

First off, thank you for considering contributing to the Chimera ML project! Whether it's reporting a bug, discussing improvements, or contributing code, your involvement is valuable. This document outlines how to contribute effectively.

## Table of Contents

*   [Code of Conduct](#code-of-conduct)
*   [How Can I Contribute?](#how-can-i-contribute)
    *   [Reporting Bugs](#reporting-bugs)
    *   [Suggesting Enhancements](#suggesting-enhancements)
    *   [Asking Questions](#asking-questions)
    *   [Contributing Code](#contributing-code)
*   [Development Setup](#development-setup)
*   [Coding Standards](#coding-standards)
*   [Pull Request Process](#pull-request-process)
*   [Testing](#testing)
*   [Documentation](#documentation)

## Code of Conduct

This project and everyone participating in it are governed by the [Chimera Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to `[]`.

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug, please check the [bug report](bug_report.md) first to see if it has already been reported. If not, please open a new issue using the "Bug Report" template. Provide as much detail as possible, including:

*   A clear and descriptive title.
*   Steps to reproduce the bug.
*   Expected behavior.
*   Actual behavior.
*   Environment details (OS, Python version, library versions).
*   Relevant logs or tracebacks.

### Suggesting Enhancements

If you have an idea for an improvement or a new feature:

1.  Check the [feature requests](feature_request.md) for existing suggestions.
2.  If your idea is new, open an issue using the "Feature Request" template.
3.  Clearly describe the enhancement, the motivation behind it (use case), and potential implementation ideas.

### Asking Questions

If you have questions about the project, usage, or architecture, please use the [issue tracker][ISSUE_TRACKER.md] with an appropriate label or use our designated communication channel `[e.g., Slack Channel, Mailing List]`.

### Contributing Code

We welcome code contributions! Here's the general workflow:

1.  **Find an issue:** Look for issues tagged with `help wanted` or `good first issue`, or discuss a new contribution idea by opening an issue first.
2.  **Fork the repository:** Create your own copy of the `chimera-ml` repository on GitHub.
3.  **Create a branch:** Create a descriptive branch name from the `main` (or `develop` if used) branch (e.g., `feature/add-csp-component` or `fix/filter-bug-123`).
    ```bash
    git checkout main
    git pull origin main
    git checkout -b feature/your-feature-name
    ```
4.  **Set up your development environment:** See [Development Setup](#development-setup).
5.  **Make your changes:** Implement your feature or fix the bug.
6.  **Write tests:** Add unit and/or integration tests for your changes. See [Testing](#testing).
7.  **Ensure checks pass:** Run linters and tests locally. See [Coding Standards](#coding-standards) and [Testing](#testing).
    ```bash
    make lint  # Or relevant commands like: pre-commit run --all-files
    make test  # Or relevant commands like: pytest
    ```
8.  **Update documentation:** If your changes affect documentation or add new features, update relevant files in `/docs` or add docstrings. See [Documentation](#documentation).
9.  **Commit your changes:** Use clear and concise commit messages. Consider the [Conventional Commits](https://www.conventionalcommits.org/) format.
    ```bash
    git add .
    git commit -m "feat: Add Common Spatial Pattern feature extractor"
    ```
10. **Push to your fork:**
    ```bash
    git push origin feature/your-feature-name
    ```
11. **Open a Pull Request (PR):** Go to the original `chimera` repository and open a PR from your fork's branch to the `main` (or `develop`) branch. Fill out the PR template provided.
12. **Code Review:** Project maintainers will review your PR. Address any feedback or requested changes.
13. **Merge:** Once approved and CI checks pass, a maintainer will merge your PR.

## Development Setup

We use [Poetry](https://python-poetry.org/) for dependency management and packaging.

1.  **Install Poetry:** Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).
2.  **Clone your fork:**
    ```bash
    git clone git@github.com:your-username/chimera-ml.git
    cd chimera-ml
    ```
3.  **Install dependencies (including dev dependencies):**
    ```bash
    poetry install --all-extras  # Or specify extras if needed
    ```
    This creates a virtual environment and installs all required packages listed in `pyproject.toml`.
4.  **Activate the virtual environment:**
    ```bash
    poetry shell
    ```
5.  **(Optional) Install pre-commit hooks:**
    ```bash
    pre-commit install
    ```
    This will automatically run linters/formatters before each commit.
6.  **(If using DVC) Pull data:**
    ```bash
    dvc pull data/01_raw # Pull specific data needed for development
    # or dvc pull to get all tracked data/models
    ```

## Coding Standards

*   **Style Guide:** We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
*   **Formatting:** We use [Black](https://github.com/psf/black) for automated code formatting.
*   **Linting:** We use [Flake8](https://flake8.pycqa.org/en/latest/) for linting (checking for style errors and potential bugs).
*   **Import Sorting:** We use [isort](https://pycqa.github.io/isort/) to keep imports organized.
*   **Type Hinting:** Use type hints (`PEP 484`) wherever practical to improve code clarity and enable static analysis.
*   **Docstrings:** Use [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for modules, classes, and functions.

These checks are often enforced via `pre-commit` hooks and CI pipelines.

## Pull Request Process

1.  Ensure your PR addresses an existing issue or has been discussed.
2.  Use a clear title and description, referencing the related issue (e.g., "Closes #123"). Use the [PR template][Link to PR Template in .github/].
3.  Ensure all CI checks (linting, testing) are passing.
4.  Keep PRs focused on a single logical change. Avoid large, monolithic PRs.
5.  Be responsive to feedback during the code review process.
6.  Once approved, a maintainer will merge the PR. Do not merge your own PRs unless explicitly allowed.

## Testing

*   Tests are located in the `/tests` directory.
*   We use [pytest](https://docs.pytest.org/) as the test runner.
*   **Unit Tests (`/tests/unit`):** Test individual functions or classes in isolation. Mock dependencies as needed.
*   **Integration Tests (`/tests/integration`):** Test the interaction between multiple components (e.g., a full data processing pipeline).
*   Aim for high test coverage, especially for core logic (`processing`, `features`, `models`).
*   Run tests using:
    ```bash
    pytest  # Or: make test
    ```

## Documentation

*   Public functions, classes, and modules should have clear docstrings (Google style).
*   Major features, architectural decisions, and usage guides should be documented in the `/docs` directory using Markdown.
*   If you add or change functionality, update the relevant documentation.
*   API documentation might be auto-generated from docstrings using tools like Sphinx with `sphinx.ext.napoleon`.

Thank you for contributing!

[Link to Issue Tracker]: https://github.com/[Your Org or Username]/chimera-ml/issues
[Link to PR Template in .github/]: ./.github/pull_request_template.md
