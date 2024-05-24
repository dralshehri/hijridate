# HijriDate

<!-- start description -->

> formerly `hijri-converter`

HijriDate is a Python package for converting between Hijri and Gregorian dates using the Umm al-Qura calendar. The package has been thoroughly verified and tested against original references to ensure its accuracy and reliability. It has an intuitive design, allows rich comparison and basic formatting of Hijri dates, and is optimized for performance.

<!-- end description -->

<!-- start badges -->

[![Release Status](https://img.shields.io/github/actions/workflow/status/dralshehri/hijridate/pypi-release.yml?label=release)][release] [![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage] [![PyPI Downloads](https://img.shields.io/pypi/dm/hijri-converter?color=blue)][downloads] [![PyPI Version](https://img.shields.io/pypi/v/hijridate)][pypi-version] [![Conda Version](https://img.shields.io/conda/vn/conda-forge/hijridate)][conda-version] [![Package License](https://img.shields.io/github/license/dralshehri/hijridate)][license] [![Package DOI](https://img.shields.io/badge/doi-10.5281%2Fzenodo.11200950-blue) ][doi]

[release]: https://github.com/dralshehri/hijridate/actions/workflows/pypi-release.yml
[coverage]: https://github.com/dralshehri/hijridate/actions/workflows/pypi-release.yml
[downloads]: https://pypistats.org/packages/hijri-converter
[pypi-version]: https://pypi.python.org/pypi/hijridate
[conda-version]: https://anaconda.org/conda-forge/hijridate
[license]: https://github.com/dralshehri/hijridate/blob/main/LICENSE
[doi]: https://doi.org/10.5281/zenodo.11200950

<!-- end badges -->

<!-- start summary -->

## Features

- Accurate and verified Hijri-Gregorian date conversion.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of the methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar era notations.
- Easily extendable to support other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.8+ with zero dependencies.
- Thoroughly tested with 100% test coverage.

## Limitations

- The date range supported by converter is limited to the period from the beginning of 1343 AH (1 August 1924 CE) to the end of 1500 AH (16 November 2077 CE).
- The conversion is not intended for religious purposes where sighting of the lunar crescent at the beginning of Hijri month is still preferred.

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

Please refer to <https://hijridate.readthedocs.io> for complete documentation on this package, which includes background information, benchmarking, usage examples, and API reference.

## Contributing

If you're interested in contributing, please check out the [Contributing](https://github.com/dralshehri/hijridate/blob/main/CONTRIBUTING.md) guide for more information on how you can help!

## License

This project is licensed under the terms of the MIT license.

<!-- start attrs -->

## Acknowledgements

- [R.H. van Gent](http://www.staff.science.uu.nl/~gent0113) &mdash; inspiration, scientific guidance and resources.
- [@AZalshehri7](https://github.com/AZalshehri7) &mdash; support in dates review and conversion accuracy verification.

## Citation

If you plan to cite this project in your academic publication, please refer to <https://doi.org/10.5281/zenodo.11200950> for citation information.
