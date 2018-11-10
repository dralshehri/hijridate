.PHONY: clean clean-build clean-pyc clean-test install build

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

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build
	rm -fr dist
	rm -fr .eggs
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .pytest_cache
	rm -f .coverage
	rm -fr htmlcov

install: clean
	pip install -q -U pip setuptools pytest pytest-cov black wheel twine
	pip install -q -e .

test:
	pytest

test-all:
	pytest tests/*

coverage:
	pytest --cov --cov-report term --cov-report html
	$(BROWSER) htmlcov/index.html

format:
	black --line-length 79 src tests setup.py

build: clean
	python setup.py sdist bdist_wheel

deploy: build
	twine upload dist/*
