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
   image:: https://img.shields.io/readthedocs/hijriconverter/latest.svg
   :alt: Docs Status
   :target: https://hijriconverter.readthedocs.io/
.. |supported|
   image:: https://img.shields.io/pypi/pyversions/hijriconverter.svg
   :alt: Python version support
   :target: https://pypi.python.org/pypi/hijriconverter
.. |version|
   image:: https://img.shields.io/pypi/v/hijriconverter.svg
   :alt: PyPI Package version
   :target: https://pypi.python.org/pypi/hijriconverter
.. |license|
   image:: https://img.shields.io/github/license/dralshehri/hijri-converter.svg
   :alt: License
   :target: https://github.com/dralshehri/hijri-converter/blob/master/LICENSE

.. contents::
   :local:
   :backlinks: none

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
the gap, `Hijri Converter`_ comes with a pythonic code, more accuracy, and
better performance.

Benchmarking
------------

Similar Python converters have been mainly derived from or using the
`Umalqurra`_ package by Khalid Al-hussayen, which was ported from `Hijri.js`_,
a Javascript tool published by Suhail Alkowaileet. The last goes back to
`R.H. van Gent`_, who built the original converter partly based on his
astronomical calculation for years after 1420 AH and partly on a comparison
calendar published by KFUPM in 1993 for the years 1356-1411 AH.

In contrast, the Hijri Converter package was written in Python from scratch.
Although it was inspired by R.H. van Gent's work, it is based on the
`Umm al-Qura calendar dataset`_ published by Mohammed Alshehri, one that is in
complete alignment with the official Umm al-Qura calendar. That makes it more
accurate and broader in terms of years included, 1300-1500 AH.

When it comes to performance, even though Hijri Converter package does extra
date validations, its conversion from Hijri to Gregorian and back is four times
faster than that of Umalqurra package.

.. code-block:: bash

   $ python -m timeit -s "from hijriconverter import convert" \
   > "convert.Gregorian(1982, 8, 4).to_hijri()" \
   > "convert.Hijri(1402, 10, 15).to_gregorian()"
   # 50000 loops, best of 5: 8.23 usec per loop

   $ python -m timeit -s "from umalqurra.hijri import Umalqurra" \
   > "Umalqurra().gegorean_to_hijri(1982, 8, 4)" \
   > "Umalqurra().hijri_to_gregorian(1402, 10, 15)"
   # 10000 loops, best of 5: 36.9 usec per loop

The above code illustrates the execution time of both packages compared
*(tested on Macbook Pro with 2.9 GHz Intel Core i5 processor and 16 GB memory)*.

In addition to the packaging and maintenance issues that Umalqurra package has,
the following table summarizes the main differences:

+---------------------------+-------------------+-------------------+
|         Item              |  Hijri Converter  |     Umalqurra     |
+===========================+===================+===================+
| Years included            | 1300-1500 AH      | 1356-1500 AH      |
+---------------------------+-------------------+-------------------+
| Accuracy (tested against  | 100%              | 93%               |
| the official calendar, not|                   |                   |
| including missing years)  |                   |                   |
+---------------------------+-------------------+-------------------+
| Performance               | 4x faster         | 1x                |
+---------------------------+-------------------+-------------------+
| Rich comparison between   | Yes               | No                |
| dates                     |                   |                   |
+---------------------------+-------------------+-------------------+
| Date validation           | Yes               | Limited           |
+---------------------------+-------------------+-------------------+
| Code testing              | Yes               | No                |
+---------------------------+-------------------+-------------------+

.. _Hijri Converter: https://pypi.org/project/hijriconverter/
.. _Umalqurra: https://pypi.org/project/umalqurra/
.. _Hijri.js: https://github.com/xsoh/Hijri.js
.. _`R.H. van Gent`: http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm
.. _Umm al-Qura calendar dataset: https://github.com/dralshehri/ummalqura-calendar

Features
--------

- Accurate and reliable conversion.
- Complete alignment with the official calendar.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar notations.
- Easily extendable for other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.6+ with zero dependencies.
- Thoroughly tested on all supported python versions.

.. note::
   The conversion is valid for dates between beginning of 1300 AH
   (11 November 1882 CE) and end of 1500 AH (16 November 2077 CE).

Online Demo
-----------

The following website implements a simple conversion tool using this package:

https://www.dralshehri.com/hijri-converter/

Installation
------------

.. code-block:: bash

   $ pip install -U hijriconverter

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
   Hijri(1403, 2, 17)

The :obj:`convert.Gregorian` object inherits all attributes and methods of
:obj:`datetime.date` object:

.. code-block:: pycon

   # To get today's date in Hijri
   >>> convert.Gregorian.today().to_hijri()
   Hijri(1440, 9, 14)

   # To format a Gregorian date
   >>> convert.Gregorian(1982, 12, 2).strftime("%A, %-d %B %Y")
   'Thursday, 2 December 1982'

Rich comparison (==, !=, >, >=, <, <=) for :obj:`convert.Hijri` objects
are also supported:

.. code-block:: pycon

   >>> convert.Hijri(1403, 2, 17) > convert.Hijri(1402, 2, 17)
   True

   >>> today_hijri = convert.Gregorian.today().to_hijri()
   >>> convert.Hijri.fromisoformat("1403-02-17") < today_hijri
   True

To convert from/to ISO format:

.. code-block:: pycon

   >>> convert.Hijri.fromisoformat("1403-02-17").to_gregorian().isoformat()
   '1982-12-02'

   >>> convert.Gregorian.fromisoformat("1982-12-02").to_hijri().isoformat()
   '1403-02-17'

You can construct a :obj:`convert.Gregorian` object from :obj:`datetime.date`
object:

.. code-block:: pycon

   >>> from datetime import date
   >>> my_date = date(1982, 12, 2)
   >>> convert.Gregorian.fromdate(my_date)
   Gregorian(1982, 12, 2)

The :obj:`convert.Hijri` object has some other useful methods. For example:

.. code-block:: pycon

   >>> hijri = convert.Gregorian(1982, 12, 2).to_hijri()

   >>> hijri.datetuple()
   (1403, 2, 17)

   >>> hijri.slashformat()
   '17/02/1403'

   >>> hijri.month_name()
   'Safar'

   >>> hijri.day_name()
   'Thursday'

   >>> hijri.notation()
   'AH'

The above example methods can also be applied to :obj:`convert.Gregorian`
object.

Date Validation
---------------

Date input values are by default checked if valid and within conversion
range. Invalid date raises a ``ValueError`` exception, and out of range date
raises an ``OverflowError`` exception. They can be caught and handled in
``try`` and ``except`` blocks:

.. code-block:: pycon

   >>> from hijriconverter import convert

   >>> convert.Hijri(1403, 1, 30)
   Traceback...
   ValueError: day must be in 1..29 for month

   >>> convert.Gregorian(1882, 12, 2).to_hijri()
   Traceback...
   OverflowError: date is out of range for conversion

Internationalization
--------------------

Representation of weekday names, month names, and calendar notations is
supported. Currently, Arabic and English translations are available, but it
can be easily extended for other natural languages.

The English is the default language and following is an example showing how
to use the Arabic language instead:

.. code-block:: pycon

   >>> from hijriconverter import convert

   >>> hijri = convert.Hijri(1403, 2, 17)

   >>> hijri.month_name("ar")
      'صفر'
   >>> hijri.day_name("ar")
      'الخميس'
   >>> hijri.notation("ar")
      'هـ'

Source Code
-----------

The source code of this package is available on
`GitHub <https://github.com/dralshehri/hijri-converter>`__
where you can contribute and report issues.

Authors
-------

The main author is Mohammed Alshehri —
`Website <https://www.dralshehri.com/>`__.

Acknowledgment
--------------

Thanks to `R.H. van Gent <http://www.staff.science.uu.nl/~gent0113>`__
for inspiration and help.

Licence
-------

This package is distributed under an MIT licence.
The licence is as follows:

.. literalinclude:: ../LICENSE
   :language: text

API Reference
-------------

This section documents the API of `convert` module, which is the main module
of Hijri Converter package.

.. automodule:: convert
