---
hide-toc: true
---

# Usage Examples

:::{eval-rst}
.. module:: convert
:::

To convert between Hijri and Gregorian dates:

```pycon
>>> from hijri_converter import convert

>>> convert.Hijri(1403, 2, 17).to_gregorian()
Gregorian(1982, 12, 2)

>>> convert.Gregorian(1982, 12, 2).to_hijri()
Hijri(1403, 2, 17)
```

To convert from/to ISO format:

```pycon
>>> from hijri_converter import convert

>>> convert.Hijri.fromisoformat('1403-02-17').to_gregorian().isoformat()
'1982-12-02'

>>> convert.Gregorian.fromisoformat('1982-12-02').to_hijri().isoformat()
'1403-02-17'
```

The {obj}`Hijri` and {obj}`Gregorian` objects have some useful methods. For
example:

```pycon
>>> from hijri_converter import convert

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
```

You can also construct a {obj}`Gregorian` object from {obj}`datetime.date`
object:

```pycon
>>> from hijri_converter import convert
>>> from datetime import date

>>> my_date = date(1982, 12, 2)
>>> convert.Gregorian.fromdate(my_date)
Gregorian(1982, 12, 2)
```

The {obj}`Gregorian` object inherits all attributes and methods of
{obj}`datetime.date` object:

```pycon
>>> from hijri_converter import convert

# To get today's date in Hijri
>>> convert.Gregorian.today().to_hijri()
Hijri(1440, 10, 13)

# To format a Gregorian date
>>> convert.Gregorian(1982, 12, 2).strftime(''%A, %-d %B %Y'')
'Thursday, 2 December 1982'
```

## Rich Comparison

Rich comparison (==, !=, >, >=, <, <=) for {obj}`Hijri` objects is supported.
Both operands should be {obj}`Hijri` objects. Otherwise, a `TypeError`
exception may be raised where it can be caught and handled in `try` and `except`
blocks: For example:

```pycon
>>> from hijri_converter import convert

>>> convert.Hijri(1403, 2, 17) > convert.Hijri(1402, 2, 17)
True

>>> convert.Hijri.fromisoformat('1403-02-17') > '1402-02-17'
Traceback (most recent call last):
...
...
TypeError: '>' not supported between instances of 'Hijri' and 'str'
```

## Internationalization

Representation of weekday names, month names, and calendar notations is
supported. The English is the default language. Currently, Arabic and Bangla translations are available, but it
can be easily extended for other natural languages.

The following is an example showing how
to use the Arabic language:

```pycon
>>> from hijri_converter import convert

>>> hijri = convert.Hijri(1403, 2, 17)

>>> hijri.month_name('ar')
'صفر'

>>> hijri.day_name('ar')
'الخميس'

>>> hijri.notation('ar')
'هـ'
```

## Date Validation

Date input values are by default checked if valid and within conversion range.
Invalid date raises a `ValueError` exception, and out of range date raises
an `OverflowError` exception. Both exceptions can be caught and handled in `try`
and `except` blocks:

```pycon
>>> from hijri_converter import convert

>>> convert.Hijri(1403, 1, 30)
Traceback (most recent call last):
...
...
ValueError: day must be in 1..29 for month

>>> convert.Gregorian(1882, 12, 2).to_hijri()
Traceback (most recent call last):
...
...
OverflowError: date out of range
```
