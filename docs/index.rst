Hijri Converter
===============

`Source Code <https://github.com/dralshehri/hijri-converter>`__

A Python package to convert Hijri date to/from Gregorian date using
`Umm al-Qura calendar`_ of Saudi Arabia.

.. _`Umm al-Qura calendar`:
   http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm

.. contents::
   :local:
   :backlinks: none

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

.. note::
    The conversion is valid for dates between beginning of 1356 AH
    (14 March 1937 CE) and end of 1500 AH (16 November 2077 CE).

Installation
------------

.. code-block:: bash

   pip install hijriconverter

Basic Usage
-----------

To import the package:

.. code-block:: pycon

   >>> from hijriconverter import convert

To convert between Hijri and Gregorian dates:

.. code-block:: pycon

   >>> convert.Hijri(1403, 2, 17).to_gregorian()
   datetime.date(1982, 12, 2)

   >>> convert.Gregorian(1982, 12, 2).to_hijri()
   Hijri(1403, 2, 17, lunar)

By default, conversion from/to Hijri date will assume Hijri lunar calendar.
To use Hijri solar calendar instead:

.. code-block:: pycon

   >>> convert.Hijri(1361, 3, 11, 'solar').to_gregorian()
   datetime.date(1982, 12, 2)

   >>> convert.Gregorian(1982, 12, 2).to_hijri('solar')
   Hijri(1361, 3, 11, solar)

The instance of Hijri date object has some other useful methods:

.. code-block:: pycon

   >>> hijri = convert.Hijri(1403, 2, 17)

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

The Gregorian date converted from Hijri date is actually an instance of
:obj:`datetime.date` object and therefore inherits all of its attributes
and methods:

.. code-block:: pycon

   >>> gregorian = convert.Hijri(1403, 2, 17).to_gregorian()

   >>> gregorian.isoformat()
   '1982-12-02'

   >>> gregorian.strftime('%A %d %b %Y')
   'Thursday 02 Dec 1982'

To validate date values and check if date is within valid conversion range,
change the `validate` parameter to ``True``. Invalid date will raise an exception that can be caught and handled in
try and except blocks:

.. code-block:: pycon

   >>> convert.Hijri(1403, 1, 30, validate=True)
   Traceback...
   ValueError: day must be in 1..29 for month

   >>> convert.Gregorian(1882, 12, 2, validate=True)
   Traceback...
   ValueError: date is out of range for conversion

Licence
-------

The package is distributed under an MIT licence.
The text is as follows (from LICENSE.txt):

.. code-block:: text

    Copyright (c) 2018 Mohammed Alshehri (dralshehri)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Credits
-------

- The Umm al-Qura Calendar of Saudi Arabia by Robert Harry van Gent.
  `Link <http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm>`__
- Julian Day Numbers by Peter Meyer.
  `Link <https://www.hermetic.ch/cal_stud/jdn.htm>`__

Convert API
-----------

This section documents the API of convert module, which is the main module of
Hijri Converter package.

.. automodule:: convert
