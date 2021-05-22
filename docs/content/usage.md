---
hide-toc: true
---

# Usage Examples

:::{eval-rst}
.. module:: convert
:::

To convert between Hijri and Gregorian dates:

```python
from hijri_converter import convert

convert.Hijri(1403, 2, 17).to_gregorian()
# Output: Gregorian(1982, 12, 2)

convert.Gregorian(1982, 12, 2).to_hijri()
# Output: Hijri(1403, 2, 17)
```

To convert from/to ISO format:

```python
from hijri_converter import convert

convert.Hijri.fromisoformat("1403-02-17").to_gregorian().isoformat()
# Output: '1982-12-02'

convert.Gregorian.fromisoformat("1982-12-02").to_hijri().isoformat()
# Output: '1403-02-17'
```

The {obj}`Hijri` and {obj}`Gregorian` objects have some useful methods. For
example:

```python
from hijri_converter import convert

hijri = convert.Gregorian(1982, 12, 2).to_hijri()

hijri.datetuple()
# Output: (1403, 2, 17)

hijri.dmyformat()
# Output: '17/02/1403'

hijri.month_name()
# Output: 'Safar'

hijri.day_name()
# Output: 'Thursday'

hijri.notation()
# Output: 'AH'
```

You can also construct a {obj}`Gregorian` object from {obj}`datetime.date`
object:

```python
from hijri_converter import convert
from datetime import date

my_date = date(1982, 12, 2)
convert.Gregorian.fromdate(my_date)
# Output: Gregorian(1982, 12, 2)
```

The {obj}`Gregorian` object inherits all attributes and methods of
{obj}`datetime.date` object:

```python
from hijri_converter import convert

# To get today's date in Hijri
convert.Gregorian.today().to_hijri()
# Output: Hijri(1440, 10, 13)

# To format a Gregorian date
convert.Gregorian(1982, 12, 2).strftime("%A, %-d %B %Y")
# Output: 'Thursday, 2 December 1982'
```

## Rich Comparison

Rich comparison (==, !=, >, >=, <, <=) for {obj}`Hijri` objects is supported.
Both operands should be {obj}`Hijri` objects. Otherwise, a `TypeError`
exception may be raised where it can be caught and handled in `try` and `except`
blocks: For example:

```python
from hijri_converter import convert

convert.Hijri(1403, 2, 17) > convert.Hijri(1402, 2, 17)
# Output: True

convert.Hijri.fromisoformat("1403-02-17") > "1402-02-17"
# Output: TypeError: '>' not supported between instances of 'Hijri' and 'str'
```

## Internationalization

Representation of weekday names, month names, and calendar notations is
supported. Currently, Arabic and English translations are available, but it
can be easily extended for other natural languages.

The English is the default language, and following is an example showing how
to use the Arabic language instead:

```python
from hijri_converter import convert

hijri = convert.Hijri(1403, 2, 17)

hijri.month_name("ar")
# Output: 'صفر'

hijri.day_name("ar")
# Output: 'الخميس'

hijri.notation("ar")
# Output: 'هـ'
```

## Date Validation

Date input values are by default checked if valid and within conversion range.
Invalid date raises a `ValueError` exception, and out of range date raises
an `OverflowError` exception. Both exceptions can be caught and handled in `try`
and `except` blocks:

```python
from hijri_converter import convert

convert.Hijri(1403, 1, 30)
# Output: ValueError: day must be in 1..29 for month

convert.Gregorian(1882, 12, 2).to_hijri()
# Output: OverflowError: date out of range
```
