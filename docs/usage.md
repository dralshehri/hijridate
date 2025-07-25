---
hide-toc: true
---

# Usage Guide

```{eval-rst}
.. currentmodule:: hijridate.convert
```

This guide demonstrates the functionality and capabilities of HijriDate for Hijri-Gregorian date conversion and manipulation. For API reference details, see the [API Documentation](api.md).

## Basic Conversions

### Simple Date Conversion

```pycon
>>> from hijridate import Hijri, Gregorian

# Convert Hijri to Gregorian
>>> Hijri(1403, 2, 17).to_gregorian()
Gregorian(1982, 12, 2)

# Convert Gregorian to Hijri
>>> Gregorian(1982, 12, 2).to_hijri()
Hijri(1403, 2, 17)
```

### Working with Today's Date

```pycon
>>> from hijridate import Hijri, Gregorian

# Get today in Hijri
>>> Hijri.today()
Hijri(1445, 6, 15)

# Get today in Gregorian and convert
>>> Gregorian.today().to_hijri()
Hijri(1445, 6, 15)
```

### ISO Format Support

For standardized date representation:

```pycon
>>> from hijridate import Hijri, Gregorian

# Parse and convert ISO format
>>> Hijri.fromisoformat('1403-02-17').to_gregorian().isoformat()
'1982-12-02'

>>> Gregorian.fromisoformat('1982-12-02').to_hijri().isoformat()
'1403-02-17'
```

## Date Formatting & Display

### Date Components and Formatting

```pycon
>>> from hijridate import Hijri

>>> hijri = Hijri(1403, 2, 17)

# Access date components
>>> hijri.year, hijri.month, hijri.day
(1403, 2, 17)

>>> hijri.datetuple()
(1403, 2, 17)

# ISO format (default string representation)
>>> hijri.isoformat()
'1403-02-17'

>>> str(hijri)
'1403-02-17'

# Day-month-year format
>>> hijri.dmyformat()
'17/02/1403'

>>> hijri.dmyformat('.', padding=False)
'17.2.1403'
```

### Month and Day Information

```pycon
>>> from hijridate import Hijri

>>> hijri = Hijri(1403, 2, 17)

# Month and day names
>>> hijri.month_name()
'Safar'

>>> hijri.day_name()
'Thursday'

# Calendar notation
>>> hijri.notation()
'AH'

# Date lengths
>>> hijri.month_length()
30

>>> hijri.year_length()
355
```

### Gregorian Integration

HijriDate's Gregorian objects inherit all standard `datetime.date` functionality:

```pycon
>>> from datetime import date
>>> from hijridate import Gregorian

# Create from standard date object
>>> my_date = date(1982, 12, 2)
>>> greg = Gregorian.fromdate(my_date)
>>> greg.to_hijri()
Hijri(1403, 2, 17)

# Use standard strftime formatting
>>> Gregorian(1982, 12, 2).strftime('%A, %B %d, %Y')
'Thursday, December 02, 1982'

# Access all datetime.date methods
>>> greg.weekday()  # Monday is 0
3

>>> greg.isoweekday()  # Monday is 1
4
```

## Internationalization

HijriDate provides multilingual support for date representation:

### Supported Languages

- **English** (`en`) - Default
- **Arabic** (`ar`) - العربية
- **Bangla** (`bn`) - বাংলা
- **Turkish** (`tr`) - Türkçe

### Multilingual Examples

```pycon
>>> from hijridate import Hijri

>>> hijri = Hijri(1403, 2, 17)

# Arabic localization
>>> hijri.month_name('ar')
'صفر'

>>> hijri.day_name('ar')
'الخميس'

>>> hijri.notation('ar')
'هـ'

# Bangla localization
>>> hijri.month_name('bn')
'সফর'

>>> hijri.day_name('bn')
'বৃহস্পতিবার'

# Turkish localization
>>> hijri.month_name('tr')
'Safer'

>>> hijri.day_name('tr')
'Perşembe'
```

## Date Comparisons

Date objects support comparison operations for sorting and conditional logic:

```pycon
>>> from hijridate import Hijri

# Date comparisons
>>> Hijri(1403, 2, 17) > Hijri(1402, 2, 17)
True

>>> Hijri(1403, 2, 17) == Hijri(1403, 2, 17)
True

>>> Hijri(1403, 1, 1) <= Hijri(1403, 12, 29)
True

# Sorting dates
>>> dates = [Hijri(1403, 6, 15), Hijri(1402, 1, 1), Hijri(1404, 12, 29)]
>>> sorted(dates)
[Hijri(1402, 1, 1), Hijri(1403, 6, 15), Hijri(1404, 12, 29)]

# Hashable objects (can be used in sets and as dict keys)
>>> date_set = {Hijri(1403, 2, 17), Hijri(1404, 3, 18)}
>>> len(date_set)
2
```

### Type Safety

Comparisons are type-safe and will raise appropriate errors:

```pycon
>>> Hijri.fromisoformat('1403-02-17') > '1402-02-17'
Traceback (most recent call last):
    ...
TypeError: '>' not supported between instances of 'Hijri' and 'str'
```

## Date Validation

HijriDate provides robust validation for data integrity:

### Automatic Validation

All date inputs are automatically validated:

```pycon
>>> from hijridate import Hijri, Gregorian

# Invalid day for month
>>> Hijri(1403, 1, 30)
Traceback (most recent call last):
    ...
ValueError: day must be in 1-29 for month, got '30'

# Invalid month
>>> Hijri(1403, 13, 15)
Traceback (most recent call last):
    ...
ValueError: month must be in 1-12, got '13'
```

### Range Validation

Dates outside the supported range are caught:

```pycon
>>> Gregorian(1882, 12, 2).to_hijri()
Traceback (most recent call last):
    ...
OverflowError: date must be in '1924-08-01'-'2077-11-16', got '1882-12-02'

>>> Hijri(1600, 1, 1).to_gregorian()
Traceback (most recent call last):
    ...
OverflowError: year must be in 1343-1500, got '1600'
```

### Bypassing Validation

For performance-critical applications, validation can be bypassed:

```pycon
>>> from hijridate import Hijri

# Skip validation for trusted input
>>> hijri = Hijri(1403, 2, 17, validate=False)
```

```{warning}
Bypassing validation does not guarantee accuracy of conversion. This approach is only recommended for dates that have already been validated externally. Invalid dates may produce incorrect conversions or unexpected behavior.
```

## Advanced Use Cases

### Julian Day Number Conversion

```pycon
>>> from hijridate import Hijri, Gregorian

>>> hijri = Hijri(1403, 2, 17)
>>> jdn = hijri.to_julian()
>>> jdn
2445334

>>> gregorian = Gregorian(1982, 12, 2)
>>> gregorian.to_julian()
2445334
```

### Working with Weekdays

```pycon
>>> from hijridate import Hijri

>>> hijri = Hijri(1403, 2, 17)

# Weekday (Monday = 0)
>>> hijri.weekday()
3

# ISO weekday (Monday = 1)
>>> hijri.isoweekday()
4

>>> hijri.day_name()
'Thursday'
```

### Error Handling Best Practices

```python
from hijridate import Gregorian

def safe_convert_to_hijri(year, month, day):
    """Safely convert Gregorian date to Hijri with error handling."""
    try:
        gregorian = Gregorian(year, month, day)
        return gregorian.to_hijri()
    except ValueError as e:
        print(f"Invalid date: {e}")
        return None
    except OverflowError as e:
        print(f"Date out of range: {e}")
        return None

# Usage
result = safe_convert_to_hijri(2024, 1, 1)
if result:
    print(f"New Year 2024 is {result.dmyformat()} in Hijri")
```

## Generating Calendar Data

For applications requiring bulk date conversion or calendar generation:

```python
import csv
from datetime import date, timedelta
from hijridate import Gregorian
from hijridate.ummalqura import GREGORIAN_RANGE


def generate_calendar(filename):
    """Generate a complete calendar mapping between Hijri and Gregorian dates."""
    start, end = GREGORIAN_RANGE
    start_date = date(*start)
    end_date = date(*end)

    with open(filename, mode='w', newline='') as file:
        calendar_writer = csv.writer(file)
        calendar_writer.writerow(["jdn", "hy", "hm", "hd", "gy", "gm", "gd"])

        row_date = start_date
        while row_date <= end_date:
            gy, gm, gd = row_date.timetuple()[:3]
            gregorian = Gregorian(gy, gm, gd)
            hy, hm, hd = gregorian.to_hijri().datetuple()
            jdn = gregorian.to_julian()  # Julian Day Number
            calendar_writer.writerow([jdn, hy, hm, hd, gy, gm, gd])
            row_date += timedelta(days=1)


if __name__ == '__main__':
    generate_calendar("ummalqura-calendar.csv")
```

This generates a CSV file with all supported dates containing:

- `jdn`: Julian Day Number
- `hy`, `hm`, `hd`: Hijri year, month, day
- `gy`, `gm`, `gd`: Gregorian year, month, day
