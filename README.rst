Hijri Converter
===============

|travis| |codecov| |supported-versions| |version|

.. |travis|
    image:: https://travis-ci.org/dralshehri/hijri-converter.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/dralshehri/hijri-converter
.. |codecov|
    image:: https://codecov.io/github/dralshehri/hijri-converter/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/dralshehri/hijri-converter
.. |supported-versions|
    image:: https://img.shields.io/pypi/pyversions/hijriconverter.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/hijriconverter
.. |version|
    image:: https://img.shields.io/pypi/v/hijriconverter.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/hijriconverter
    
A Python library to convert Hijri_ (Islamic) date to/from Gregorian date using
Umm al-Qura calendar of Saudi Arabia.

.. _Hijri: https://en.wikipedia.org/wiki/Islamic_calendar

Features
--------

- Support for both lunar and solar Hijri calendars.
- Validation of date input.
- Easy and intuitive usage.
- English/Arabic representation of Hijri months and days.
- Very accurate and reliable calculation.
- Reviewed and fully tested against multiple references, including:

  * Official website of Umm al-Qura calendar of Saudi Arabia.
    `[Link] <http://www.ummulqura.org.sa/default.aspx>`__
  * Comparison Calendar (1356 AH - 1411 AH) published by Research Institute,
    King Fahd University of Petroleum & Minerals, Saudi Arabia.
    `[Link] <https://www.staff.science.uu.nl/~gent0113/islam/downloads/ksa_calendar_1356_1411.pdf>`__

Installation
------------

::

    pip install hijriconverter

Usage
-----

To import the library:

.. code-block:: python

    from hijriconverter import convert

To convert between Hijri and Gregorian dates:

.. code-block:: python

    convert.Hijri(1403, 2, 17).to_gregorian()
    # datetime.date(1982, 12, 2)

    convert.Gregorian(1982, 12, 2).to_hijri()
    # Hijri(1403, 2, 17, lunar)

By default, conversion from/to Hijri date will assume Hijri lunar calendar.
To use Hijri solar calendar instead:

.. code-block:: python

    convert.Hijri(1361, 3, 11, 'solar').to_gregorian()
    # datetime.date(1982, 12, 2)

    convert.Gregorian(1982, 12, 2).to_hijri('solar')
    # Hijri(1361, 3, 11, solar)

The instance of Hijri date object has some other useful attributes and methods:

.. code-block:: python

    hijri = convert.Hijri(1403, 2, 17)

    hijri.isoformat()
    # '1403-02-17'

    hijri.datetuple()
    # (1403, 2, 17)

    hijri.month_days()
    # 30

    hijri.month_name()
    # 'Safar'

    hijri.weekday()
    # 3

    hijri.isoweekday()
    # 4

    hijri.day_name()
    # 'Thursday'

The Gregorian date converted from Hijri date is actually an instance of
`datetime.date`_ object and therefore inherits all of its attributes and
methods:

.. _`datetime.date`: https://docs.python.org/3/library/datetime.html#date-objects

.. code-block:: python

    gregorian = convert.Hijri(1403, 2, 17).to_gregorian()

    gregorian.isoformat()
    # '1982-12-02'

    gregorian.strftime('%A %d %b %Y')
    # 'Thursday 02 Dec 1982'

Documentation
-------------

**Hijri Object**

A Hijri object represents a Hijri date (year, month and day) in lunar or solar
Hijri calendar.

+-----------------------------------------------------------------------------+
| class **Hijri**\ (*year, month, day, calendar='lunar'*)                     |
+-----------------------------------------------------------------------------+
|| The *year*, *month* and *day* arguments are required and must be integers. |
|| The *calendar* argument is optional and must be a string.                  |
| It may be 'lunar' or 'solar'. Default is 'lunar'.                           |
+-----------------------------------------------------------------------------+

*Instance attributes:*

+-----------------------------------------------------------------------------+
| Hijri.\ **year**                                                            |
+-----------------------------------------------------------------------------+
| Return the year as an integer.                                              |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **month**                                                           |
+-----------------------------------------------------------------------------+
| Return the month as an integer.                                             |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **day**                                                             |
+-----------------------------------------------------------------------------+
| Return the day as an integer.                                               |
+-----------------------------------------------------------------------------+

*Instance methods:*

+-----------------------------------------------------------------------------+
| Hijri.\ **isoformat**\ ()                                                   |
+-----------------------------------------------------------------------------+
| Return a string representing the date in ISO format ‘YYYY-MM-DD’.           |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **datetuple**\ ()                                                   |
+-----------------------------------------------------------------------------+
| Return the date as a tuple of (year, month, day).                           |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **month_days**\ ()                                                  |
+-----------------------------------------------------------------------------+
| Return the number of days in the month as an integer.                       |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **month_name**\ (*language='en'*)                                   |
+-----------------------------------------------------------------------------+
|| Return month name as a string in specified language.                       |
|| The language argument is optional and must be a string.                    |
| It may be 'en' for English or 'ar' for Arabic. Default is 'en'.             |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **weekday**\ ()                                                     |
+-----------------------------------------------------------------------------+
| Return the day of the week as an integer, where Monday is 0 and Sunday is 6.|
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **isoweekday**\ ()                                                  |
+-----------------------------------------------------------------------------+
| Return the day of the week as an integer, where Monday is 1 and Sunday is 7.|
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **day_name**\ (*language='en'*)                                     |
+-----------------------------------------------------------------------------+
|| Return day name as a string in specified language.                         |
|| The language argument is optional and must be a string.                    |
| It may be 'en' for English or 'ar' for Arabic. Default is 'en'.             |
+-----------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+
| Hijri.\ **to_gregorian**\ ()                                                |
+-----------------------------------------------------------------------------+
| Return a converted gregorian date as a datetime.date object.                |
+-----------------------------------------------------------------------------+

----

**Gregorian Object**

A Gregorian object represents a Gregorian date (year, month and day) in
Gregorian calendar.

+-----------------------------------------------------------------------------+
| class **Gregorian**\ (*year, month, day*)                                   |
+-----------------------------------------------------------------------------+
| The *year*, *month* and *day* arguments are required and must be integers.  |
+-----------------------------------------------------------------------------+

*Instance methods:*

+-----------------------------------------------------------------------------+
| Gregorian.\ **to_hijri**\ (*calendar='lunar'*)                              |
+-----------------------------------------------------------------------------+
|| Return a converted Hijri date as a Hijri object.                           |
|| The *calendar* argument is optional and must be a string.                  |
| It may be 'lunar' or 'solar'. Default is 'lunar'.                           |
+-----------------------------------------------------------------------------+

Limitations
-----------

The conversion is valid for dates between beginning of 1356 AH
(14 March 1937 CE) and end of 1500 AH (16 November 2077 CE).

Credits
-------

- The Umm al-Qura Calendar of Saudi Arabia by Robert Harry van Gent.
  `[Link] <http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm>`__
- Julian Day Numbers by Peter Meyer.
  `[Link] <https://www.hermetic.ch/cal_stud/jdn.htm>`__
