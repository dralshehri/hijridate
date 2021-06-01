# Contributing

Any contribution is welcome, and it's much appreciated! Every little helps, and a credit will always be given.

## Reporting Issues

An issue may be a simple comment, question, feature request, or bug report. When [reporting an issue](https://github.com/dralshehri/hijri-converter/issues/new), please make sure to provide enough information to understand it.

## Changing Code

You may want to make some changes to the package codebase. For example, to fix a bug, to add a new feature, or to update documentation. You can do so by following these simple steps:
1. Fork [GitHub repository](https://github.com/dralshehri/hijri-converter).
2. Clone your repository locally.
3. Make your code changes.
4. Push it back to your repository.
5. Create a pull request on GitHub.

## Developing Locally

The following are some commands you may need to use when coding on a local machine. It's assumed that you have created and activated a virtual environment with Python 3.9 or newer.

### Install dependencies:

```shell
pip install -U -r requirements-dev.txt
```

### Run tests:

```shell
# for essential unit tests
pytest

# for full (unit and data) tests
pytest tests
```

### Measure code coverage:

```shell
# Terminal report only
pytest --cov

# Terminal and HTML reports
pytest --cov --cov-report term --cov-report html
```

### Check type annotations:

```shell
mypy src
```

### Format code and sort imports:

```shell
black src tests
isort src tests
```

### Generate documentation:

```shell
sphinx-build -E -b dirhtml docs docs/_build
```

### Build package:

```shell
python -m build --sdist --wheel
```

## Need Help?
In case you feel like you've made a valuable contribution, but you don't know how to write or run tests for it, or how to generate the documentation: don't let this discourage you from making the pull request; I can help you! Just go ahead and submit the pull request, but keep in mind that you might be asked to append additional commits to your pull request.
