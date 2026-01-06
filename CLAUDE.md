# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python package for accurate Hijri-Gregorian date conversion using the Umm al-Qura calendar.

### Core Structure
- **`src/hijridate/`** - Main package code
  - `convert.py` - Core `Hijri` and `Gregorian` classes with conversion logic
  - `ummalqura.py` - Umm al-Qura calendar data and calculations
  - `helpers.py` - Utility functions for Julian day number conversions
  - `locales.py` - Multilingual support for month names and weekdays

### Key Classes
- **`Hijri`** - Represents dates in the Hijri (lunar) calendar
- **`Gregorian`** - Represents dates in the Gregorian (solar) calendar
- Both classes provide bidirectional conversion via `.to_gregorian()` and `.to_hijri()` methods

### Limitations
- **Date Range**: Supports dates from 1343 AH (1 August 1924 CE) to 1500 AH (16 November 2077 CE) only
- **Religious Context**: Not intended for religious purposes where lunar crescent sighting is preferred

## Development

The project uses `uv` as the package manager. Run `uv sync` to set up the environment.

### Commands
```bash
uv run ruff format       # Format code
uv run ruff check --fix  # Lint code
uv run mypy              # Type check
uv run pytest --cov      # Test with coverage
```

### Testing Structure
- `tests/unit/` - Unit tests for individual modules
- `tests/integration/` - Integration tests against reference data
- Fixtures in `tests/integration/fixtures/` contain verified reference calendars

## Code Quality Standards

- **100% test coverage** is required - coverage will fail if below 100%
- **Type hints** are mandatory for all functions and methods
- **Ruff** is used for both formatting and linting
- **MyPy** runs in strict mode
- **Google docstring style** for all public APIs

## Critical Constraints

- **Zero runtime dependencies** - do not add any
- **Conversion accuracy is critical** - validate against reference data in integration tests
- **Performance matters** - this is an optimized library