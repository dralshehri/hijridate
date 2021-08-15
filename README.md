# Hijri Converter

<!-- start description -->

A Python package to convert accurately between Hijri and Gregorian dates
based on astronomical calculation of the Umm al-Qura calendar.

<!-- end description -->

[![Checks Status](https://img.shields.io/github/workflow/status/dralshehri/hijri-converter/Checks/main?event=push&label=checks)][checks]
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage]
[![Code Quality](https://img.shields.io/codefactor/grade/github/dralshehri/hijri-converter/main?&label=codefactor)][quality]
[![Docs Status](https://img.shields.io/readthedocs/hijri-converter/stable)][docs]
[![PyPI Downloads](https://img.shields.io/pypi/dm/hijri-converter?color=blue)][downloads]
[![PyPI Version](https://img.shields.io/pypi/v/hijri-converter)][version]
[![Package License](https://img.shields.io/github/license/dralshehri/hijri-converter)][license]

[checks]: https://github.com/dralshehri/hijri-converter/actions/workflows/checks.yml
[coverage]: https://github.com/dralshehri/hijri-converter/actions/workflows/checks.yml
[quality]: https://www.codefactor.io/repository/github/dralshehri/hijri-converter/overview/main
[docs]: https://hijri-converter.readthedocs.io
[downloads]: https://pypistats.org/packages/hijri-converter
[version]: https://pypi.python.org/pypi/hijri-converter
[license]: https://github.com/dralshehri/hijri-converter/blob/main/LICENSE

<!-- start summary -->

## Features

- Accurate and tested date conversion.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of the methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar notations.
- Easily extendable to support other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.6+ with zero dependencies.
- Thoroughly tested on all supported python versions.

## Limitations

- The date range supported by converter is limited to the period from the beginning
  of 1343 AH (1 August 1924 CE) to the end of 1500 AH (16 November 2077 CE).
- The conversion is not intended for religious purposes where sighting of the lunar
  crescent at the beginning of Hijri month is still preferred.

## Installation

```shell
pip install -U hijri-converter
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

## Changelog

All notable changes to this package are documented in 
[CHANGELOG.md](https://github.com/dralshehri/hijri-converter/blob/main/CHANGELOG.md).

## Contributing

Contributions are always welcome! See [CONTRIBUTING.md](https://github.com/dralshehri/hijri-converter/blob/main/CONTRIBUTING.md)
for ways to get started.

<!-- start footer -->

## Acknowledgements

* [R.H. van Gent](http://www.staff.science.uu.nl/~gent0113) &mdash; inspiration, scientific guidance and resources.
* [@AZalshehri7](https://github.com/AZalshehri7) &mdash; support in dates review and conversion validation.

## License

This package is distributed under an MIT license.
See [LICENSE](https://github.com/dralshehri/hijri-converter/blob/main/LICENSE).

<!-- end footer -->
