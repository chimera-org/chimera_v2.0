.PHONY: help clean lint format test test-unit test-integration test-cov install setup-dev docs notebook requirements dvc-pull

# Default target when running `make`
help:
	@echo "Available commands:"
	@echo "  make install         - Install dependencies using Poetry"
	@echo "  make setup-dev       - Install dev dependencies and pre-commit hooks"
	@echo "  make requirements    - Export pinned dependencies to requirements.txt"
	@echo "  make clean           - Remove cache files, build artifacts"
	@echo "  make lint            - Run linters (flake8, isort check, black check)"
	@echo "  make format          - Format code using black and isort"
	@echo "  make test            - Run all tests with pytest"
	@echo "  make test-unit       - Run only unit tests"
	@echo "  make test-integration - Run only integration tests"
	@echo "  make test-cov        - Run all tests and show coverage report"
	@echo "  make docs            - Build documentation (if using Sphinx/MkDocs)"
	@echo "  make notebook        - Start Jupyter Lab"
	@echo "  make dvc-pull        - Pull DVC tracked data/models"

# Variables
PYTHON = poetry run python
PYTEST = poetry run pytest
BLACK = poetry run black
ISORT = poetry run isort
FLAKE8 = poetry run flake8
PRECOMMIT = poetry run pre-commit
DVC = poetry run dvc
# SPHINXBUILD = poetry run sphinx-build # Example for Sphinx
# MKDOCSBUILD = poetry run mkdocs build # Example for MkDocs

# Project structure assumptions
SRC_DIR = src/chimera_ml
TEST_DIR = tests
UNIT_TEST_DIR = tests/unit
INTEGRATION_TEST_DIR = tests/integration
DOC_SOURCE_DIR = docs
DOC_BUILD_DIR = docs/_build # Example for Sphinx

# Installation and Setup
install: pyproject.toml poetry.lock
	poetry install --no-dev

setup-dev: pyproject.toml poetry.lock
	poetry install --all-extras # Or specify relevant extras
	$(PRECOMMIT) install

requirements: pyproject.toml poetry.lock
	poetry export --without-hashes -f requirements.txt -o requirements.txt --with dev

dvc-pull:
	$(DVC) pull

# Cleaning
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache .mypy_cache build dist *.egg-info .coverage htmlcov $(DOC_BUILD_DIR)

# Linting and Formatting
lint:
	@echo "Running isort check..."
	$(ISORT) --check-only --diff .
	@echo "Running black check..."
	$(BLACK) --check --diff .
	@echo "Running flake8..."
	$(FLAKE8) $(SRC_DIR) $(TEST_DIR)

format:
	@echo "Running isort..."
	$(ISORT) .
	@echo "Running black..."
	$(BLACK) .

# Testing
test:
	$(PYTEST) $(TEST_DIR)

test-unit:
	$(PYTEST) $(UNIT_TEST_DIR)

test-integration:
	$(PYTEST) $(INTEGRATION_TEST_DIR)

test-cov:
	$(PYTEST) --cov=$(SRC_DIR) --cov-report=term-missing --cov-report=html $(TEST_DIR)
	@echo "Coverage report available in htmlcov/index.html"

# Documentation (adjust commands based on your tool)
docs:
	@echo "Building documentation..."
	# Example for Sphinx: $(SPHINXBUILD) -b html $(DOC_SOURCE_DIR) $(DOC_BUILD_DIR)
	# Example for MkDocs: $(MKDOCSBUILD)
	@echo "Documentation build requires Sphinx or MkDocs setup."

# Notebooks
notebook:
	poetry run jupyter lab
