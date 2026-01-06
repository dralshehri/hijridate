# HijriDate

<!-- start description -->

> formerly `hijri-converter`

A Python package for accurate Hijri-Gregorian date conversion using the Umm al-Qura calendar.

HijriDate provides reliable date conversion based on official sources, including archived Umm al-Qura newspaper publications and comparative calendar data from King Abdulaziz City for Science and Technology (KACST). The package has been thoroughly tested and verified against original references to ensure accuracy and reliability.

<!-- end description -->

<!-- start badges -->

[![Release Status](https://img.shields.io/badge/release-pass-success)][release] [![Coverage Status](https://img.shields.io/badge/coverage-100%25-success)][coverage] [![PyPI Downloads](https://static.pepy.tech/badge/hijri-converter)][downloads] [![PyPI Version](https://img.shields.io/pypi/v/hijridate)][pypi-version] [![Conda Version](https://img.shields.io/conda/vn/conda-forge/hijridate)][conda-version] [![Package License](https://img.shields.io/github/license/dralshehri/hijridate)][license] [![Package DOI](https://img.shields.io/badge/doi-10.5281%2Fzenodo.11200950-blue) ][doi]

[release]: https://github.com/dralshehri/hijridate/releases/latest
[coverage]: https://github.com/dralshehri/hijridate/releases/latest
[downloads]: https://pepy.tech/project/hijri-converter
[pypi-version]: https://pypi.python.org/pypi/hijridate
[conda-version]: https://anaconda.org/conda-forge/hijridate
[license]: https://github.com/dralshehri/hijridate/blob/main/LICENSE
[doi]: https://doi.org/10.5281/zenodo.11200950

<!-- end badges -->

<!-- start summary -->

## ✨ Features

- Accurate and verified Hijri-Gregorian date conversion
- Based on official Umm al-Qura calendar sources and archived publications
- Optimized performance compared to existing implementations
- Comprehensive input validation and error handling
- Multilingual support for Arabic, English, and other languages
- Rich comparison operations and date formatting options
- Full type annotations and 100% test coverage
- Zero runtime dependencies

## ⚠️ Limitations

**Date Range**: The converter supports dates from 1343 AH to 1500 AH (1 August 1924 CE to 16 November 2077 CE), corresponding to the period covered by available official calendar sources.

**Religious Context**: Not intended for religious purposes where lunar crescent sighting is preferred over astronomical calculations.

## 📦 Installation

To install using `uv`, run:

```shell
uv add hijridate
```

To install using `pip`, run:

```shell
pip install hijridate
```

To install using `conda`, run:

```shell
conda install -c conda-forge hijridate
```

## 🚀 Basic Usage

```python
from hijridate import Hijri, Gregorian

# Convert a Hijri date to Gregorian
hijri_date = Hijri(1445, 6, 15)
gregorian_date = hijri_date.to_gregorian()
print(gregorian_date)  # 2023-12-28

# Convert a Gregorian date to Hijri
gregorian_date = Gregorian(2023, 12, 28)
hijri_date = gregorian_date.to_hijri()
print(hijri_date)  # 1445-06-15
```

<!-- end summary -->

## 📚 Documentation

Please refer to <https://hijridate.readthedocs.io> for complete documentation on this package, which includes background information, benchmarking, usage examples, and API reference.

## 🤝 Contributing

If you're interested in contributing, please check out the [Contributing](https://github.com/dralshehri/hijridate/blob/main/CONTRIBUTING.md) guide for more information on how you can help!

## 📄 License

This project is licensed under the terms of the MIT license.

<!-- start attrs -->

## 🙏 Acknowledgements

- [R.H. van Gent](http://www.staff.science.uu.nl/~gent0113) &mdash; inspiration, scientific guidance and resources.
- [@AZalshehri7](https://github.com/AZalshehri7) &mdash; support in dates review and conversion accuracy verification.

## 📝 Citation

If you plan to cite this project in your academic publication, please refer to <https://doi.org/10.5281/zenodo.11200950> for citation information.
