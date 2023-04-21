# Contributing

Any contribution is welcome, and it's much appreciated! Every little helps, and
a credit will always be given.

## Reporting Issues

An issue may be a simple comment, question, feature request, or bug report. When
[reporting an issue], please make sure to provide enough information to
understand it.

[reporting an issue]: https://github.com/dralshehri/hijri-converter/issues/new

## Changing Code

You may want to make some changes to the project codebase. For example, to fix a
bug, to add a new feature, or to update documentation. You can do so by
following these simple steps:

1. Fork the [project repository] on GitHub.
2. Clone your fork to your local machine.
3. Add the [project repository] as the "upstream" remote.
4. Create a new branch from the `develop` branch.
5. Make your changes, format code, and run tests.
6. Pull the latest changes from upstream.
7. Commit and push your changes to your fork.
8. Create a pull request on GitHub and select the `develop` base branch.

[project repository]: https://github.com/dralshehri/hijri-converter

## Developing Locally

The following are some commands you may need to use when coding on a local
machine. It's assumed that you have already created and activated a **virtual
environment** with Python 3.10 or newer.

### Preparing for development:

The project and development dependencies can be installed using:

```shell
pip install -r requirements-dev.txt && pip install -e .
```

### Formatting code:

After changing code, run the formatter to ensure consistency:

```shell
task format
```

### Running tests and quality checks:

Before committing changes, make sure to pass all tests and quality checks:

```shell
task test
task lint
```

## Compiling documentation:

To build and browse documentation locally, run:

```shell
pip install -r docs/requirements.txt
sphinx-build -E docs docs/_build
```

The resulting HTML can be found in `docs/_build`

## Need Help?

Don't let anything discourage you from making the pull request. I can help you!
Just go ahead and submit the pull request.
