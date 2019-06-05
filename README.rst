Hijri Converter
===============

A Python package to convert accurately between Hijri and Gregorian dates
using the Umm al-Qura calendar of Saudi Arabia.

|travis| |codecov| |docs| |supported| |version| |license|

.. |travis|
   image:: https://img.shields.io/travis/com/dralshehri/hijri-converter.svg
   :alt: Build Status
   :target: https://travis-ci.com/dralshehri/hijri-converter
.. |codecov|
   image:: https://img.shields.io/codecov/c/github/dralshehri/hijri-converter.svg
   :alt: Coverage Status
   :target: https://codecov.io/github/dralshehri/hijri-converter
.. |docs|
   image:: https://img.shields.io/readthedocs/hijri-converter/stable.svg
   :alt: Docs Status
   :target: https://hijri-converter.readthedocs.io/
.. |supported|
   image:: https://img.shields.io/pypi/pyversions/hijri-converter.svg
   :alt: Python version support
   :target: https://pypi.python.org/pypi/hijri-converter
.. |version|
   image:: https://img.shields.io/pypi/v/hijri-converter.svg
   :alt: PyPI Package version
   :target: https://pypi.python.org/pypi/hijri-converter
.. |license|
   image:: https://img.shields.io/github/license/dralshehri/hijri-converter.svg
   :alt: License
   :target: https://github.com/dralshehri/hijri-converter/blob/master/LICENSE

Overview
--------

The Umm al-Qura calendar is the lunar Hijri (Islamic) calendar officially
adopted by Saudi Arabia for administrative purposes. It is mainly used by the
government, including its health care and education systems, in which almost
all documents and transactions are dated by the Hijri calendar.

However, the Gregorian calendar is the calendar used in most of the world,
and it has been implemented as the default calendar in nearly every computer
and database.

Therefore, a valid converter between Hijri and Gregorian dates is a necessity,
especially when conducting research, analyzing data, or building applications
that may have Hijri dates. Even though similar packages exist and try to fill
the gap, `Hijri Converter <https://github.com/dralshehri/hijri-converter>`__
comes with a pythonic code, more accuracy, and better performance.

Features
--------

- Accurate and reliable conversion.
- Complete alignment with the official calendar.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar notations.
- Easily extendable to support other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.6+ with zero dependencies.
- Thoroughly tested on all supported python versions.

Online Demo
-----------

The following website implements a simple conversion tool using this package:

https://www.dralshehri.com/hijri-converter/

Installation
------------

.. code-block:: bash

   $ pip install -U hijri-converter

Basic Usage
-----------

.. code-block:: python

   from hijri_converter import convert

   g = convert.Hijri(1403, 2, 17).to_gregorian()
   print(g)
   # 1982-12-02

   h = convert.Gregorian(1982, 12, 2).to_hijri()
   print(h)
   # 1403-02-17

Documentation
-------------

Please see https://hijri-converter.readthedocs.io/ for full documentation of
this package, including benchmarking, usage examples and API reference.

Contributing
------------

Contributions are welcome! See
`CONTRIBUTING.rst <https://github.com/dralshehri/hijri-converter/blob/master/CONTRIBUTING.rst>`__
for more info.

Authors
-------

The main author is Mohammed Alshehri —
`Website <https://www.dralshehri.com/>`__.

Acknowledgment
--------------

Thanks to `R.H. van Gent <http://www.staff.science.uu.nl/~gent0113>`__
for inspiration and help.

License
-------

This package is distributed under an MIT license.
See `LICENSE <https://github.com/dralshehri/hijri-converter/blob/master/LICENSE>`__.
