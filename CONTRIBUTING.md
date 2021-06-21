# Contributing

Any contribution is welcome, and it's much appreciated! Every little helps,
and a credit will always be given.

## Reporting Issues

An issue may be a simple comment, question, feature request, or bug report.
When [reporting an issue](https://github.com/dralshehri/hijri-converter/issues/new),
please make sure to provide enough information to understand it.

## Changing Code

You may want to make some changes to the package codebase. For example, to fix a bug,
to add a new feature, or to update documentation.
You can do so by following these simple steps:
1. Fork [GitHub repository](https://github.com/dralshehri/hijri-converter).
2. Clone your repository locally.
3. Make your code changes on the `develop` branch.
4. Push it back to your repository.
5. Create a pull request on GitHub.

## Developing Locally

The following are some commands you may need to use when coding on a local machine.
It's assumed that you have already created and activated a virtual environment with
Python 3.9 or newer.

### Preparing for development:

The project and all required packages can be installed using:

```shell
pip install -r requirements-dev.txt -e .
```

### Formatting code:

After changing code, run the formatter to ensure consistency:

```shell
task format
```

### Compiling documentation:

To build and browse documentation locally, run:

```shell
task docs
```

The resulting HTML can be found in `docs/_build/html`

### Running tests and quality checks:

Before committing changes, make sure to pass all tests and quality checks:

```shell
task test
task lint
```

## Need Help?
Don't let anything to discourage you from making the pull request.
I can help you! Just go ahead and submit the pull request.
