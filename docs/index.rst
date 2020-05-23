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

.. contents::
   :local:
   :backlinks: none

.. module:: convert

Overview
--------

The Umm al-Qura calendar is the lunar Hijri calendar officially adopted by
Saudi Arabia for administrative purposes. It was originated from Umm al-Qura
newspaper, the official newspaper of government of Saudi Arabia. The newspaper
is published weekly and its first issue was on Friday, 15 Jumada al-Ula 1343 AH
(12 December 1924 CE). However, the calendar has been printed and distributed
separately by the Saudi government since 1346 AH (1927 CE).

The calendar is widely used in Saudi Arabia, especially by the governmental
sector. Official documents, political letters, health care records, and
education certificates, are just examples of many other documents that are
dated by the Hijri calendar.

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
calendar prepared by KFUPM in 1993 for the years 1356-1411 AH.

In contrast, the *Hijri Converter* package was written in Python from scratch.
Although it was inspired by R.H. van Gent's work, it is mainly based on the
Umm al-Qura newspaper issues published weekly since 1343 AH, one that is in
complete alignment with the official printed Umm al-Qura calendar. However,
other sources was also used to build the package including the comparison
calendar prepared by KFUPM for the years 1356-1411 AH, and the official website
of Umm al-Qura calendar for the years 1431-1500 AH. Both sources were also
verified using the dates of then-published issues of Umm al-Qura newspaper.
That makes *Hijri Converter* package more accurate and broader in terms of
years included, 1343-1500 AH.

When it comes to performance, using *Hijri Converter* package to convert from
Hijri to Gregorian and back is seven times faster (or five times faster, with
Hijri date validation enabled) than that when *Umalqurra* package was used.

.. code-block:: bash

   # Hijri Converter with Hijri date validation disabled
   $ python -m timeit -s "from hijri_converter import convert" \
   > "convert.Gregorian(1982, 8, 4).to_hijri()" \
   > "convert.Hijri(1402, 10, 15).to_gregorian()"
   50000 loops, best of 5: 5.4 usec per loop

   # Hijri Converter with Hijri date validation enabled
   $ python -m timeit -s "from hijri_converter import convert" \
   > "convert.Gregorian(1982, 8, 4).to_hijri()" \
   > "convert.Hijri(1402, 10, 15).to_gregorian()"
   50000 loops, best of 5: 7.6 usec per loop

   # Umalqurra without Hijri date validation
   $ python -m timeit -s "from umalqurra.hijri import Umalqurra" \
   > "Umalqurra().gegorean_to_hijri(1982, 8, 4)" \
   > "Umalqurra().hijri_to_gregorian(1402, 10, 15)"
   50000 loops, best of 5: 37.6 usec per loop

The above code illustrates the execution time of both packages compared
*(tested on Macbook Pro with 2.9GHz Intel Core i5 processor and 16GB memory)*.

Beside packaging and maintenance issues that *Umalqurra* package
has, the following table summarizes the main differences:

+---------------------------+-------------------+-------------------+
|         Item              |  Hijri Converter  |     Umalqurra     |
+===========================+===================+===================+
| Years included            | 1343-1500 AH      | 1356-1500 AH      |
+---------------------------+-------------------+-------------------+
| Accuracy [#]_             | 100%              | 91.6%             |
+---------------------------+-------------------+-------------------+
| Performance [#]_          | 7x (faster)       | 1x                |
+---------------------------+-------------------+-------------------+
| Python 3 support          | Full              | Limited           |
+---------------------------+-------------------+-------------------+
| Rich comparison between   | Yes               | No                |
| dates                     |                   |                   |
+---------------------------+-------------------+-------------------+
| Hijri date validation     | Yes               | No                |
+---------------------------+-------------------+-------------------+
| Code testing              | Yes               | No                |
+---------------------------+-------------------+-------------------+

.. _Hijri Converter: https://pypi.org/project/hijri-converter/
.. _Umalqurra: https://pypi.org/project/umalqurra/
.. _Hijri.js: https://github.com/xsoh/Hijri.js
.. _`R.H. van Gent`: http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm

Features
--------

- Accurate and tested conversion.
- Optimized code performance compared to similar packages.
- Intuitive, clean, and easy-to-use interface.
- Most of methods and formats are similar to those of standard library.
- Multilingual representation of weekday names, months, and calendar notations.
- Easily extendable to support other natural languages.
- Rich comparison between dates.
- Validation of input dates.
- Works on Python 3.6+ with zero dependencies.
- Thoroughly tested on all supported python versions.

.. note::
   The conversion is valid for dates from the beginning of 1343 AH
   (1 August 1924 CE) to the end of 1500 AH (16 November 2077 CE).

Installation
------------

.. code-block:: bash

   $ pip install -U hijri-converter

Usage Examples
--------------

To import the package:

.. code-block:: pycon

   >>> from hijri_converter import convert

To convert between Hijri and Gregorian dates:

.. code-block:: pycon

   >>> convert.Hijri(1403, 2, 17).to_gregorian()
   Gregorian(1982, 12, 2)

   >>> convert.Gregorian(1982, 12, 2).to_hijri()
   Hijri(1403, 2, 17)

To convert from/to ISO format:

.. code-block:: pycon

   >>> convert.Hijri.fromisoformat("1403-02-17").to_gregorian().isoformat()
   '1982-12-02'

   >>> convert.Gregorian.fromisoformat("1982-12-02").to_hijri().isoformat()
   '1403-02-17'

The :obj:`Hijri` and :obj:`Gregorian` objects have some useful methods. For
example:

.. code-block:: pycon

   >>> hijri = convert.Gregorian(1982, 12, 2).to_hijri()

   >>> hijri.datetuple()
   (1403, 2, 17)

   >>> hijri.dmyformat()
   '17/02/1403'

   >>> hijri.month_name()
   'Safar'

   >>> hijri.day_name()
   'Thursday'

   >>> hijri.notation()
   'AH'

You can also construct a :obj:`Gregorian` object from :obj:`datetime.date`
object:

.. code-block:: pycon

   >>> from datetime import date
   >>> my_date = date(1982, 12, 2)
   >>> convert.Gregorian.fromdate(my_date)
   Gregorian(1982, 12, 2)

The :obj:`Gregorian` object inherits all attributes and methods of
:obj:`datetime.date` object:

.. code-block:: pycon

   # To get today's date in Hijri
   >>> convert.Gregorian.today().to_hijri()
   Hijri(1440, 10, 13)

   # To format a Gregorian date
   >>> convert.Gregorian(1982, 12, 2).strftime("%A, %-d %B %Y")
   'Thursday, 2 December 1982'

Rich Comparison
~~~~~~~~~~~~~~~

Rich comparison (==, !=, >, >=, <, <=) for :obj:`Hijri` objects is supported.
Comparing :obj:`Hijri` object with different type object raises a ``TypeError``
exception that can be caught and handled in ``try`` and ``except`` blocks:

.. code-block:: pycon

   >>> convert.Hijri(1403, 2, 17) > convert.Hijri(1402, 2, 17)
   True

   >>> convert.Hijri.fromisoformat("1403-02-17") == "1403-02-17"
   Traceback...
   TypeError: can't compare 'Hijri' to 'str'


Internationalization
~~~~~~~~~~~~~~~~~~~~

Representation of weekday names, month names, and calendar notations is
supported. Currently, Arabic and English translations are available, but it
can be easily extended for other natural languages.

The English is the default language, and following is an example showing how
to use the Arabic language instead:

.. code-block:: pycon

   >>> from hijri_converter import convert

   >>> hijri = convert.Hijri(1403, 2, 17)

   >>> hijri.month_name("ar")
      'صفر'

   >>> hijri.day_name("ar")
      'الخميس'

   >>> hijri.notation("ar")
      'هـ'

Date Validation
~~~~~~~~~~~~~~~

Date input values are by default checked if valid and within conversion range.
Invalid date raises a ``ValueError`` exception, and out of range date raises
an ``OverflowError`` exception. They can be caught and handled in ``try``
and ``except`` blocks:

.. code-block:: pycon

   >>> from hijri_converter import convert

   >>> convert.Hijri(1403, 1, 30)
   Traceback...
   ValueError: day must be in 1..29 for month

   >>> convert.Gregorian(1882, 12, 2).to_hijri()
   Traceback...
   OverflowError: date out of range

Online Tool
-----------

The following is a simple online conversion tool that was developed to convert
between Hijri and Gregorian dates using the latest version of *Hijri Converter*
package:

https://www.dralshehri.com/hijri-converter/

Source Code
-----------

The source code of this package is available on
`GitHub <https://github.com/dralshehri/hijri-converter>`__ where you can
contribute and report issues.

Authors
-------

The main author is Mohammed Alshehri —
`@dralshehri <https://github.com/dralshehri>`__.

Acknowledgment
--------------

Thanks to `R.H. van Gent <http://www.staff.science.uu.nl/~gent0113>`__
for inspiration and help.

License
-------

This package is distributed under an MIT license.
The license is as follows:

.. literalinclude:: ../LICENSE
   :language: text

API Reference
-------------

This section documents the API of `convert` module, which is the main module
of the Hijri Converter package.

.. autoclass:: Hijri
.. autoclass:: Gregorian

.. [#] Verified with the years 1343-1355 AH included, which are missing from
       *Umalqurra* package but can produce wrong dates when used.
.. [#] Hijri date validation was disabled in *Hijri Converter* package; to be
       comparable with *Umalqurra* package.
