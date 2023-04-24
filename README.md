# hijridate

<!-- start description -->

A Python package to convert accurately between Hijri and Gregorian dates using
the Umm al-Qura calendar.

<!-- end description -->

<!-- start badges -->

[![Release Status](https://img.shields.io/github/actions/workflow/status/dralshehri/hijridate/release.yml?label=release)][release]
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage]
[![Code Quality](https://img.shields.io/codefactor/grade/github/dralshehri/hijridate/main?&label=codefactor)][quality]
[![Docs Status](https://img.shields.io/readthedocs/hijridate/stable)][docs]
[![PyPI Downloads](https://img.shields.io/pypi/dm/hijridate?color=blue)][downloads]
[![PyPI Version](https://img.shields.io/pypi/v/hijridate)][pypi-version]
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/hijridate)][conda-version]
[![Package License](https://img.shields.io/github/license/dralshehri/hijridate)][license]

[release]: https://github.com/dralshehri/hijridate/actions/workflows/release.yml
[coverage]:
  https://github.com/dralshehri/hijridate/actions/workflows/release.yml
[quality]:
  https://www.codefactor.io/repository/github/dralshehri/hijridate/overview/main
[docs]: https://hijridate.readthedocs.io
[downloads]: https://pypistats.org/packages/hijridate
[pypi-version]: https://pypi.python.org/pypi/hijridate
[conda-version]: https://anaconda.org/conda-forge/hijridate
[license]: https://github.com/dralshehri/hijridate/blob/main/LICENSE

<!-- end badges -->

<!-- start summary -->

## Features

- Accurate and verified date conversion.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of the methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar era
  notations.
- Easily extendable to support other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.7+ with zero dependencies.
- Thoroughly tested with 100% test coverage.

## Limitations

- The date range supported by converter is limited to the period from the
  beginning of 1343 AH (1 August 1924 CE) to the end of 1500 AH (16 November
  2077 CE).
- The conversion is not intended for religious purposes where sighting of the
  lunar crescent at the beginning of Hijri month is still preferred.

## Installation

To install using `pip`, run:

```shell
pip install hijridate
```

To install using `conda`, run:

```shell
conda install -c conda-forge hijridate
```

## Basic Usage

```python
from hijridate import Hijri, Gregorian

# Convert a Hijri date to Gregorian
g = Hijri(1403, 2, 17).to_gregorian()

# Convert a Gregorian date to Hijri
h = Gregorian(1982, 12, 2).to_hijri()
```

<!-- end summary -->

## Documentation

Please see <https://hijridate.readthedocs.io> for full documentation of this
package, including background, benchmarking, usage examples and API reference.

## License

This project is licensed under the terms of the MIT license.

## Acknowledgements

- [R.H. van Gent](http://www.staff.science.uu.nl/~gent0113) &mdash; inspiration,
  scientific guidance and resources.
- [@AZalshehri7](https://github.com/AZalshehri7) &mdash; support in dates review
  and conversion accuracy verification.
