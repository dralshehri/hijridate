# Changelog

This project follows [PEP 440](https://peps.python.org/pep-0440/) semantic versioning:

- **MAJOR** (e.g., `2.5.0` → `3.0.0`) — Breaking changes that require code updates (API changes, removed features, behavior changes)
- **MINOR** (e.g., `2.5.0` → `2.6.0`) — New features that are backward compatible
- **PATCH** (e.g., `2.5.0` → `2.5.1`) — Bug fixes and small improvements

## 2.6.0 - 2026-01-06

- Dropped support for Python 3.8 and 3.9, and added support for Python 3.13 and 3.14
- Added Turkish language support ([#25](https://github.com/dralshehri/hijridate/pull/25) by [@abdelslam1997](https://github.com/abdelslam1997))
- Replaced versioning module with a static version
- Changed type hints to modern syntax
- Changed copyright notice to a simplified format
- Updated documentation content and structure
- Updated development tools and workflows

## 2.5.0 - 2024-05-25

- Added a new function called `year_length()`, which calculates the total number of days in a Hijri year
- Changed the `validate` argument when instantiating Hijri objects to be a keyword-only argument
- Changed the `padding` argument for `dmyformat()` functions to be a keyword-only argument
- Improved exception messages to display the values provided by the user
- Improved type hints for supported natural languages
- Improved readability and documentation of several functions
- Improved reliability of some tests
- Fixed typos in English Hijri month names
- Fixed miscellaneous formatting and linting issues
- Published the package on [Zenodo](https://zenodo.org/records/11200950) to become citable by researchers
- Updated development tools, workflows, and documentation

## 2.4.1 - 2023-12-09

- Fixed some typos

## 2.4.0 - 2023-12-08

- Dropped support for Python 3.7 and added support for Python 3.12
- Fixed a typo in the Bangla translation ([#18](https://github.com/dralshehri/hijridate/pull/18) by [@nokibsarkar](https://github.com/nokibsarkar))
- Changed documentation theme along with other enhancements

## 2.3.0 - 2023-04-24

**IMPORTANT**

The `hijri-converter` package has been **renamed** to `hijridate` in preparation for the upcoming major update

Please use a version specifier e.g. `hijridate~=2.3.0` to avoid any breaking changes in the future

### What's Changed

- Renamed the package to `hijridate` and deprecated the old name
- Dropped support for Python 3.6 and added support for Python 3.11
- Updated documentation and removed badges from the package description
- Updated development configurations and GitHub actions
- Changed GitHub username back to @dralshehri and updated related links

## 2.2.4 - 2022-05-23

- Added more classifiers to package configuration
- Fixed location of type-checking marker file ([#10](https://github.com/dralshehri/hijridate/pull/10) by [@dimbleby](https://github.com/dimbleby))
- Updated development and build requirements

## 2.2.3 - 2022-02-12

- Changed package docstrings to Google style and updated documentation
- Updated development workflows and configurations
- Other minor fixes and enhancements
- Changed GitHub username to @mhalshehri and updated related links

## 2.2.2 - 2021-09-25

- Added some missing variable annotations to `ummalqura` module
- Fixed an issue when generating documentation
- Fixed some typos in docstrings and improved documentation
- Other minor fixes and enhancements

## 2.2.1 - 2021-09-04

- Fixed calculation of month 12 of the year 1354 AH
- Fixed an issue when generating documentation without the package being installed ([#7](https://github.com/dralshehri/hijridate/issues/7))
- Refactored internal helper functions
- Updated and improved tests and documentation
- Fixed some typos

## 2.2.0 - 2021-08-16

- Added `today()` classmethod to Hijri class to get the Hijri Object of today's date
- Added `separator` and `padding` parameters to `dmyformat()` method to have more control over formatting
- Refactored locales for better management and testing (Inspired by [Arrow](https://github.com/arrow-py/arrow) localization)
- Updated main classes to be conveniently imported into the package level e.g. `from hijri_converter import Hijri, Gregorian`
- Removed deprecated method `slashformat()` from Hijri and Gregorian classes
- Updated tests and documentation
- Other minor fixes and internal enhancements

## 2.1.3 - 2021-06-22

- Minor fixes and enhancements for docstrings and documentation

## 2.1.2 - 2021-05-30

- Added Bangla translation ([#4](https://github.com/dralshehri/hijridate/pull/4) by [@nokibsarkar](https://github.com/nokibsarkar))
- Changed `Hijri` rich comparison to return `NotImplemented` when the second operand is not `Hijri` class
- Changed `ummalqura` constants to be in capital letters adhering to PEP8
- Updated packaging configuration files and local development workflow
- Other minor fixes and documentation enhancements

## 2.1.1 - 2020-05-21

- Added `dmyformat()` to return dates in `DD/MM/YYYY` format
- Deprecated `slashformat()` method to be replaced by `dmyformat()` method
- Fixed PyPI package not including some required files ([#3](https://github.com/dralshehri/hijridate/issues/3))
- Fixed some typos
- Updated tests

## 2.1.0 - 2019-06-16

This version has more accurate conversion and better internal code. Details are as follows:

- Dropped support for the years before 1343 AH because the Umm al-Qura calendar was not established then
- Added `validate` parameter to Hijri class for optional disabling of Hijri date validation and improving performance. However, disabling validation will decrease the conversion accuracy silently
- Verified conversion against original references and updated the `month_starts` tuple for more accurate conversion
- Improved `Hijri` class rich comparison methods
- Improved date validation methods for better performance and readability
- Made the `Hijri` class hashable by adding a custom `__hash__` method
- Refactored many internal methods (not affecting the API)
- Other minor fixes, enhancements and performance boost

## 2.0.0 - 2019-06-05

In short, this version supports only lunar Hijri calendar on Python 3.6+, and the conversion is in complete agreement with the official Umm al-Qura calendar. Details are as follows:

- Renamed the package to `hijri-converter`
- Dropped support for the solar Hijri calendar
- Dropped support for Python 3.5
- Refactored localization and `ummalqura.py` module
- Updated `month_starts` tuple in alignment with the Umm al-Qura calendar
- Added `fromdate()` classmethod to `Gregorian` class
- Added `notation()` method to `Hijri` and `Gregorian` classes
- Added more methods to `Gregorian` class including `slashformat()`, `month_name()`, `day_name()` and `to_julian()`
- Renamed `month_days()` method of `Hijri` class to `month_length()`
- Changed formatted string to use f-strings
- Improved documentation and examples
- Updated unit tests
- Fixed other minor issues and typos

## 1.5.0 - 2018-12-27

- Added `fromisoformat()` classmethod to `Hijri` class
- Added support for rich comparison between Hijri dates
- Updated documentation and testing code
- Other minor fixes and enhancements

## 1.4.0 - 2018-11-26

- Refactored conversion methods to improve performance
- Changed date validation back to be the default and removed optional parameter
- Added `to_julian()` method to `Hijri` class
- Updated documentation and testing code
- Other minor fixes and enhancements

## 1.3.3 - 2018-11-21

- Fixed a bug in range validation for the Gregorian date
- Changed generic typing to built-in types
- Added more tests to cover the solar calendar
- Improved code structure and documentation

## 1.3.2 - 2018-11-16

- Improved documentation and changelog

## 1.3.1 - 2018-11-16

- Fixed README file

## 1.3.0 - 2018-11-16

- Added documentation directory with an online version
- Changed date input validation to be optional and disabled by default
- Improved code readability and performance
- Other minor fixes and enhancements

## 1.2.0 - 2018-11-09

- Added `slashformat()` method to `Hijri` class
- Improved date validation code
- Fixed some typos in documentation and docstrings

## 1.0.1 - 2018-10-28

- Improved examples and documentation

## 1.0.0 - 2018-10-28

- First release
