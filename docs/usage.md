---
hide-toc: true
---

# Usage Examples

```{eval-rst}
.. currentmodule:: hijridate.convert
```

To convert between Hijri and Gregorian dates:

```pycon
>>> from hijridate import Hijri, Gregorian

>>> Hijri(1403, 2, 17).to_gregorian()
Gregorian(1982, 12, 2)

>>> Gregorian(1982, 12, 2).to_hijri()
Hijri(1403, 2, 17)
```

To convert from/to ISO format:

```pycon
>>> from hijridate import Hijri, Gregorian

>>> Hijri.fromisoformat('1403-02-17').to_gregorian().isoformat()
'1982-12-02'

>>> Gregorian.fromisoformat('1982-12-02').to_hijri().isoformat()
'1403-02-17'
```

To get the today's date in Hijri:

```pycon
>>> from hijridate import Hijri

>>> Hijri.today().isoformat()
'1443-01-08'
```

The {obj}`Hijri` objects have some other useful methods. For example:

```pycon
>>> from hijridate import Hijri

>>> hijri = Hijri(1403, 2, 17)

>>> hijri.datetuple()
(1403, 2, 17)

>>> hijri.dmyformat()
'17/02/1403'

>>> hijri.dmyformat('.', False)
'17.2.1403'

>>> hijri.month_name()
'Safar'

>>> hijri.day_name()
'Thursday'

>>> hijri.notation()
'AH'
```

The above methods can also be used with {obj}`Gregorian` objects.

You can additionally construct a {obj}`Gregorian` object from
{obj}`datetime.date` object:

```pycon
>>> from datetime import date
>>> from hijridate import Gregorian

>>> my_date = date(1982, 12, 2)
>>> Gregorian.fromdate(my_date)
Gregorian(1982, 12, 2)
```

The {obj}`Gregorian` object inherits all attributes and methods of
{obj}`datetime.date` object:

```pycon
>>> from hijridate import Gregorian

# To get today's date in Hijri
>>> Gregorian.today().to_hijri()
Hijri(1440, 10, 13)

# To format a Gregorian date
>>> Gregorian(1982, 12, 2).strftime('%A, %-d %B %Y')
'Thursday, 2 December 1982'
```

## Rich Comparison

Rich comparison (==, !=, >, >=, <, <=) for {obj}`Hijri` objects is supported.
Both operands should be {obj}`Hijri` objects. Otherwise, a `TypeError` exception
may be raised where it can be caught and handled in `try` and `except` blocks:
For example:

```pycon
>>> from hijridate import Hijri

>>> Hijri(1403, 2, 17) > Hijri(1402, 2, 17)
True

>>> Hijri.fromisoformat('1403-02-17') > '1402-02-17'
Traceback (most recent call last):
    ...
TypeError: '>' not supported between instances of 'Hijri' and 'str'
```

## Internationalization

Representation of weekday names, month names, and calendar notations is
supported. English `en` is the default language. Additionally, Arabic `ar` and
Bangla `bn` translations are available, but it can be easily extended for other
natural languages.

The following is an example showing how to use the Arabic language:

```pycon
>>> from hijridate import Hijri

>>> hijri = Hijri(1403, 2, 17)

>>> hijri.month_name('ar')
'صفر'

>>> hijri.day_name('ar')
'الخميس'

>>> hijri.notation('ar')
'هـ'
```

## Date Validation

Date input values are by default checked if valid and within conversion range.
Invalid date raises a `ValueError` exception, which can be caught and handled in
`try` and `except` blocks:

```pycon
>>> from hijridate import Hijri, Gregorian

>>> Hijri(1403, 1, 30)
Traceback (most recent call last):
    ...
ValueError: day must be in 1-29 for month, got '30'

>>> Gregorian(1882, 12, 2).to_hijri()
Traceback (most recent call last):
    ...
OverflowError: date must be in '1924-08-01'-'2077-11-16', got '1882-12-02'
```
