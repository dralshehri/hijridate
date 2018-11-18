.PHONY: clean clean-test clean-pyc clean-docs clean-build help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef

export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-test clean-pyc clean-docs clean-build ## remove all artifacts

clean-test: ## remove test and coverage artifacts
	rm -fr .pytest_cache
	rm -f .coverage
	rm -fr htmlcov

clean-pyc: ## remove python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-docs: ## remove docs artifacts
	rm -fr docs/_build

clean-build: ## remove build artifacts
	rm -fr build
	rm -fr dist
	rm -fr .eggs
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

install: clean ## install dev requirments and project source
	pip install -q -U pip setuptools pytest pytest-cov black sphinx wheel twine
	pip install -q -e .

format: ## format code with black
	black -l 79 src tests setup.py

test: ## run unit tests only
	pytest

test-all: ## run unit and integration tests
	pytest tests/*

coverage: ## check code coverage
	pytest --cov --cov-report term --cov-report html
	$(BROWSER) htmlcov/index.html

docs: clean-docs ## generate html documentation
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

build: clean ## build and check project
	python setup.py sdist bdist_wheel
	twine check dist/*

deploy: build ## deploy project to pypi
	twine upload dist/*
