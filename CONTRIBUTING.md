# Contributing

Thank you for your interest in contributing to HijriDate! We welcome all types of contributions, from questions to code changes.

## Quick Start

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork locally
git clone https://github.com/YOUR_USERNAME/hijridate.git
cd hijridate

# 3. Set up development environment
uv sync

# 4. Run tests to make sure everything works
uv run pytest --cov
```

## How to Contribute

### 🤔 Questions or Ideas

- Check [Discussions](https://github.com/dralshehri/hijridate/discussions) for similar topics
- Start a new discussion if you don't find what you're looking for

### 🐛 Bug Reports

- Check [Issues](https://github.com/dralshehri/hijridate/issues) for existing reports
- Create a new issue with:
  - Version number
  - Steps to reproduce
  - Expected vs actual behavior
  - Your operating system

### 💻 Code Changes

1. **Prerequisites**: [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
2. **Setup**: Fork the repo and run `uv sync` to install dependencies
3. **Before committing**: Run these commands to ensure your changes pass all checks:
   ```bash
   uv run ruff format          # Format code
   uv run ruff check --fix     # Fix linting issues
   uv run mypy                 # Check types
   uv run pytest --cov         # Run tests with coverage
   ```
4. **Submit**: Push to your fork and create a pull request

## Development Commands

```bash
# Setup
uv sync                       # Install dependencies

# Code quality
uv run ruff format            # Format code
uv run ruff check --fix       # Fix linting issues
uv run mypy                   # Type checking

# Testing
uv run pytest                # Run all tests
uv run pytest --cov          # Run tests with coverage report

# Documentation
uv run sphinx-build -E docs docs/_build  # Build docs

# Build
uv build                     # Build distribution packages
```

## Maintainers Only

### Changelog

Add `## Unreleased` section to `CHANGELOG.md` when there are unreleased changes. The release script replaces it with the version number.

### Updating Dependencies

To update all development dependencies to their latest versions:

```bash
uv sync --upgrade
```

### Releasing

To create a new release, ensure you're on the `main` branch with all changes committed and synced with the remote:

```bash
bash release.sh <major|minor|patch>
```

## Need Help?

- Review the [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) on forking and pull requests
- Check existing [discussions](https://github.com/dralshehri/hijridate/discussions) and [issues](https://github.com/dralshehri/hijridate/issues)
- Start a new discussion for questions

We appreciate your contribution! 🎉
