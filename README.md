# Hijri Converter

<!-- start summary -->
A Python package to convert accurately between Hijri and Gregorian dates
using the Umm al-Qura calendar of Saudi Arabia.

[![Build Status](https://img.shields.io/travis/com/dralshehri/hijri-converter.svg)][build]
[![Coverage Status](https://img.shields.io/codecov/c/github/dralshehri/hijri-converter.svg)][coverage]
[![Docs Status](https://img.shields.io/readthedocs/hijri-converter/stable.svg)][docs]
[![PyPI Version](https://img.shields.io/pypi/v/hijri-converter.svg)][version]
[![PyPI Downloads](https://img.shields.io/pypi/dm/hijri-converter)][downloads]
[![Package License](https://img.shields.io/github/license/dralshehri/hijri-converter.svg)][license]

[build]: https://travis-ci.com/dralshehri/hijri-converter
[coverage]: https://codecov.io/github/dralshehri/hijri-converter
[docs]: https://hijri-converter.readthedocs.io/
[version]: https://pypi.python.org/pypi/hijri-converter
[downloads]: https://pypistats.org/packages/hijri-converter
[license]: https://github.com/dralshehri/hijri-converter/blob/main/LICENSE

## Features

- Accurate and tested conversion.
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

- The conversion is valid for dates from the beginning of 1343 AH
  (1 August 1924 CE) to the end of 1500 AH (16 November 2077 CE).
- This package is not intended for religious purposes where sighting of the lunar crescent at the beginning of Hijri month is still preferred.

## Installation

```shell
pip install -U hijri-converter
```

## Basic Usage

```python
from hijri_converter import convert

g = convert.Hijri(1403, 2, 17).to_gregorian()
print(g)
# 1982-12-02

h = convert.Gregorian(1982, 12, 2).to_hijri()
print(h)
# 1403-02-17
```
<!-- end summary -->

## Documentation

Please see <https://hijri-converter.readthedocs.io/> for full documentation of
this package, including overview, benchmarking, usage examples and API
reference.

## Changelog

All notable changes to this package are documented in 
[CHANGELOG.md](https://github.com/dralshehri/hijri-converter/blob/main/CHANGELOG.md).

## Contributing

Any contribution is welcome! Refer to
[CONTRIBUTING.md](https://github.com/dralshehri/hijri-converter/blob/main/CONTRIBUTING.md)
for instructions and local development commands.

## Authors

Authors and acknowledgments are listed in 
[AUTHORS.md](https://github.com/dralshehri/hijri-converter/blob/main/AUTHORS.md).

## License

This package is distributed under an MIT license.
See [LICENSE](https://github.com/dralshehri/hijri-converter/blob/main/LICENSE).
