Hijri Converter
===============

A Python package to convert Hijri date to/from Gregorian date using
`Umm al-Qura calendar`_ of Saudi Arabia.

.. _`Umm al-Qura calendar`:
   http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm

`Source Code <https://github.com/dralshehri/hijri-converter>`__

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

.. contents::
   :local:
   :backlinks: none

Features
--------

- Accurate and reliable conversion.
- Optimized code performance.
- Fully tested against multiple original references.
- Support for both lunar and solar Hijri calendars.
- Validation of date input.
- Easy and intuitive usage.
- English/Arabic representation of Hijri months and days.

.. note::
   The conversion is valid for dates between beginning of 1356 AH
   (14 March 1937 CE) and end of 1500 AH (16 November 2077 CE).

Installation
------------

.. code-block:: bash

   $ pip install hijriconverter

Usage Examples
--------------

To import the package:

.. code-block:: pycon

   >>> from hijriconverter import convert

To convert between Hijri and Gregorian dates:

.. code-block:: pycon

   >>> convert.Hijri(1403, 2, 17).to_gregorian()
   Gregorian(1982, 12, 2)

   >>> convert.Gregorian(1982, 12, 2).to_hijri()
   Hijri(1403, 2, 17, lunar)

By default, conversion from/to Hijri date will assume Hijri lunar calendar.
To use Hijri solar calendar instead:

.. code-block:: pycon

   >>> convert.Hijri(1361, 3, 11, "solar").to_gregorian()
   Gregorian(1982, 12, 2)

   >>> convert.Gregorian(1982, 12, 2).to_hijri("solar")
   Hijri(1361, 3, 11, solar)

The :obj:`convert.Gregorian` object inherits all attributes and methods of
:obj:`datetime.date` object:

.. code-block:: pycon

   # To get today date in Hijri
   >>> convert.Gregorian.today().to_hijri()
   Hijri(1440, 3, 18, lunar)

   # To format Gregorian date converted from Hijri
   >>> gregorian = convert.Hijri(1403, 2, 17).to_gregorian()
   >>> gregorian.strftime("%A %d %b %Y")
   'Thursday 02 Dec 1982'

The :obj:`convert.Hijri` object has some other useful methods:

.. code-block:: pycon

   >>> hijri = convert.Gregorian(1982, 12, 2).to_hijri()

   >>> hijri.datetuple()
   (1403, 2, 17)

   >>> hijri.isoformat()
   '1403-02-17'

   >>> hijri.slashformat()
   '17/02/1403'

   >>> hijri.month_days()
   30

   >>> hijri.month_name()
   'Safar'

   >>> hijri.weekday()
   3

   >>> hijri.isoweekday()
   4

   >>> hijri.day_name()
   'Thursday'

Date values are by default checked if valid and within conversion range.
Invalid date will raise a ``ValueError`` exception that can be caught and handled
in try and except blocks:

.. code-block:: pycon

   >>> convert.Hijri(1403, 1, 30)
   Traceback...
   ValueError: day must be in 1..29 for month

   >>> convert.Gregorian(1882, 12, 2)
   Traceback...
   ValueError: date is out of range for conversion

Credits
-------

- Robert Harry van Gent.
  `The Umm al-Qura Calendar of Saudi Arabia <http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm>`__.
- Peter Meyer.
  `Julian Day Numbers <https://www.hermetic.ch/cal_stud/jdn.htm>`__.

Licence
-------

This package is distributed under an MIT licence.
The licence is as follows (from ``LICENSE.txt`` file):

.. literalinclude:: ../LICENSE.txt
   :language: text

API Reference
-------------

This section documents the API of `convert` module, which is the main module
of Hijri Converter package.

.. automodule:: convert
