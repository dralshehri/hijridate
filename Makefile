SHELL := /bin/bash
.DEFAULT_GOAL := help

VENV=.venv
PYTHON=$(VENV)/bin/python

.PHONY: clean clean-test clean-pyc clean-docs clean-build install

help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
    awk -F ':.*?## ' 'NF==2 {printf "\033[34m  %-15s\033[0m %s\n", $$1, $$2}'

clean: clean-test clean-pyc clean-docs clean-build ## Remove all artifacts

clean-test: ## Remove tests artifacts
	rm -fr .pytest_cache
	rm -f .coverage
	rm -fr htmlcov

clean-docs: ## Remove docs artifacts
	rm -fr docs/_build

clean-pyc: ## Remove python artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build: ## Remove build artifacts
	rm -fr build
	rm -fr dist
	rm -fr .eggs
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

install: clean ## Install development requirments
	rm -fr .venv
	python3 -m venv .venv --copies
	$(PYTHON) -m pip install -U pip setuptools
	$(PYTHON) -m pip install -U pytest pytest-cov black sphinx wheel twine
	$(PYTHON) -m pip install -e .

format: ## Format code with Black
	$(PYTHON) -m black -l 79 -t py36 src tests setup.py

test: ## Run unit tests
	$(PYTHON) -m pytest

test-cov: ## Run tests with code coverage
	$(PYTHON) -m pytest --cov --cov-report term --cov-report html
	$(PYTHON) -m webbrowser $(PWD)/htmlcov/index.html

test-more: ## Run unit and integration tests
	$(PYTHON) -m pytest tests/*

docs: clean-docs ## Generate html documentation
	source $(VENV)/bin/activate; $(MAKE) -C docs html
	$(PYTHON) -m webbrowser $(PWD)/docs/_build/html/index.html

build: clean-build ## Build and check the package
	$(PYTHON) setup.py sdist bdist_wheel
	$(PYTHON) -m twine check dist/*

deploy: build ## Deploy the package to PyPi
	$(PYTHON) -m twine upload dist/*
