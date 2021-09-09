# hijri-converter

<!-- start description -->

A Python package to convert accurately between Hijri and Gregorian dates
using the Umm al-Qura calendar.

<!-- end description -->

[![Checks Status](https://img.shields.io/github/workflow/status/dralshehri/hijri-converter/Checks/main?event=push&label=checks)][checks]
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage]
[![Code Quality](https://img.shields.io/codefactor/grade/github/dralshehri/hijri-converter/main?&label=codefactor)][quality]
[![Docs Status](https://img.shields.io/readthedocs/hijri-converter/stable)][docs]
[![PyPI Downloads](https://img.shields.io/pypi/dm/hijri-converter?color=blue)][downloads]
[![PyPI Version](https://img.shields.io/pypi/v/hijri-converter)][pypi-version]
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/hijri-converter)][conda-version]
[![Package License](https://img.shields.io/github/license/dralshehri/hijri-converter)][license]

[checks]: https://github.com/dralshehri/hijri-converter/actions/workflows/checks.yml
[coverage]: https://github.com/dralshehri/hijri-converter/actions/workflows/checks.yml
[quality]: https://www.codefactor.io/repository/github/dralshehri/hijri-converter/overview/main
[docs]: https://hijri-converter.readthedocs.io
[downloads]: https://pypistats.org/packages/hijri-converter
[pypi-version]: https://pypi.python.org/pypi/hijri-converter
[conda-version]: https://anaconda.org/conda-forge/hijri-converter
[license]: https://github.com/dralshehri/hijri-converter/blob/main/LICENSE

<!-- start summary -->

## Features

- Accurate and verified date conversion.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of the methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar era notations.
- Easily extendable to support other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.6+ with zero dependencies.
- Thoroughly tested with 100% test coverage.

## Limitations

- The date range supported by converter is limited to the period from the beginning
  of 1343 AH (1 August 1924 CE) to the end of 1500 AH (16 November 2077 CE).
- The conversion is not intended for religious purposes where sighting of the lunar
  crescent at the beginning of Hijri month is still preferred.

## Installation

To install using `pip`, run:
```shell
pip install hijri-converter
```

To install using `conda`, run:
```shell
conda install -c conda-forge hijri-converter
```

## Basic Usage

```python
from hijri_converter import Hijri, Gregorian


# Convert a Hijri date to Gregorian
g = Hijri(1403, 2, 17).to_gregorian()

# Convert a Gregorian date to Hijri
h = Gregorian(1982, 12, 2).to_hijri()
```

<!-- end summary -->

## Documentation

Please see <https://hijri-converter.readthedocs.io> for full documentation of
this package, including background, benchmarking, usage examples and API
reference.


## License

This project is licensed under the terms of the MIT license.
