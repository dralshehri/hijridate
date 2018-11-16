Hijri Converter
===============

|travis| |codecov| |docs| |supported| |version|

.. |travis|
    image:: https://travis-ci.org/dralshehri/hijri-converter.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/dralshehri/hijri-converter
.. |codecov|
    image:: https://codecov.io/github/dralshehri/hijri-converter/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/dralshehri/hijri-converter
.. |docs|
    image:: https://readthedocs.org/projects/hijriconverter/badge/?version=latest
    :alt: Docs Status
    :target: http://hijriconverter.readthedocs.io/en/latest
.. |supported|
    image:: https://img.shields.io/pypi/pyversions/hijriconverter.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/hijriconverter
.. |version|
    image:: https://img.shields.io/pypi/v/hijriconverter.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/hijriconverter
    
A Python package to convert Hijri date to/from Gregorian date using
`Umm al-Qura calendar`_ of Saudi Arabia.

.. _`Umm al-Qura calendar`:
   http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm

Features
--------

- Support for both lunar and solar Hijri calendars.
- Accurate and reliable calculation.
- Easy and intuitive usage.
- English/Arabic representation of Hijri months and days.
- Optionally validate date input.
- Fully tested against multiple references, including:

  * `Official website`_ of Umm al-Qura calendar maintained by King Abdulaziz
    City for Science and Technology, Saudi Arabia.
  * `Comparison Calendar (1356 AH - 1411 AH)`_ published by Research Institute,
    King Fahd University of Petroleum & Minerals, Saudi Arabia.

.. _`Official website`: http://www.ummulqura.org.sa/default.aspx
.. _`Comparison Calendar (1356 AH - 1411 AH)`:
   https://www.staff.science.uu.nl/~gent0113/islam/downloads/ksa_calendar_1356_1411.pdf

Documentation
-------------

Documentation is available at https://hijriconverter.readthedocs.io and
in the ``docs`` directory.


Changelog
---------

**1.3.0 (2018-11-16)**

- Added documentation directory with an online version.
- Changed date input validation to be optional and disabled by default.
- Improved code readability and performance.
- Other minor fixes and enhancements.

**1.2.0 (2018-11-09)**

- Added `slashformat()` method to Hijri date.
- Improved date validation code
- Fixed some typos in documentation and docstrings

**1.0.1 (2018-10-28)**

- Improved examples and documentation.

**1.0.0 (2018-10-28)**

- First release.
