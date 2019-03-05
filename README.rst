Hijri Converter
===============

A Python package to convert Hijri date to/from Gregorian date using
`Umm al-Qura calendar`_ of Saudi Arabia.

.. _`Umm al-Qura calendar`:
   http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm

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

Features
--------

- Accurate and reliable conversion formula.
- Fully tested against multiple original references.
- Support for both lunar and solar Hijri calendars.
- English/Arabic representation of Hijri months and days.
- Rich comparison between Hijri dates.
- Validation of Hijri dates.
- Optimized code performance.

Demo
----

Please visit https://www.dralshehri.com/code/hijri-converter to try the
conversion function of this package as a simple usage example.

Installation
------------

.. code-block:: bash

   $ pip install -U hijriconverter

Documentation
-------------

Please see https://hijriconverter.readthedocs.io for full documentation of
this package, including usage examples and API reference.

Credits
-------

- Robert Harry van Gent.
  `The Umm al-Qura Calendar of Saudi Arabia <http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm>`__.
- Peter Meyer.
  `Julian Day Numbers <https://www.hermetic.ch/cal_stud/jdn.htm>`__.

License
-------

This package is distributed under an MIT licence. See ``LICENSE.rst`` file.
