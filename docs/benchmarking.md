---
hide-toc: true
---

# Benchmarking

This document compares HijriDate against existing Hijri conversion implementations.

## Accuracy

Most existing Python Hijri converters trace back to [R.H. van Gent's work](http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm), which combines astronomical calculations with partial calendar data. The [ummalqura package](https://pypi.org/project/ummalqura/), ported from [hijri.js](https://github.com/xsoh/Hijri.js), inherits this approach with modifications from Khalid Al-hussayen.

HijriDate was developed from scratch using systematic primary source verification:

- **1343-1355 AH**: Archived Umm al-Qura newspaper issues
- **1356-1411 AH**: KFUPM Comparison Calendar
- **1412-1450 AH**: Official Umm al-Qura Comparative Calendar books
- **1451-1500 AH**: KACST official website data

The package is tested against all 55,991 days in the supported range (1343-1500 AH / 1924-2077 CE), using 1,896 month start references from original sources:

| Package   | Correct Conversions | Total Tested | Accuracy |
| --------- | ------------------: | -----------: | -------: |
| HijriDate |              55,991 |       55,991 |   100.0% |
| ummalqura |              51,249 |       55,991 |    91.5% |

**Note**: The ummalqura package accepts dates in 1343-1355 AH but produces incorrect conversions for this period, as it lacks verified data for these years.

## Performance

Benchmark environment: Python 3.14, 1M iterations, best of 5 runs.

| Package   | Time per conversion\* | Relative speed | 1M conversions |
| --------- | --------------------: |---------------:| -------------: |
| HijriDate |                1.6 μs |     ~7x faster |           1.6s |
| ummalqura |               10.8 μs |             1x |          10.8s |

\*Two-way conversion (Hijri→Gregorian→Hijri)

```shell
# HijriDate
uv run python -m timeit -s 'from hijridate import Hijri, Gregorian' \
  -n 1000000 -r 5 'Hijri(1402, 10, 15).to_gregorian(); Gregorian(1982, 8, 4).to_hijri()'
1000000 loops, best of 5: 1.63 usec per loop

# ummalqura
uv run python -m timeit -s 'from ummalqura.hijri import Umalqurra' \
  -n 1000000 -r 5 'Umalqurra().hijri_to_gregorian(1402, 10, 15); Umalqurra().gegorean_to_hijri(1982, 8, 4)'
1000000 loops, best of 5: 10.8 usec per loop
```

## Features

Beyond performance and accuracy, HijriDate provides comprehensive functionality compared to existing implementations:

| Feature              |  HijriDate   |  ummalqura   |
| :------------------- | :----------: | :----------: |
| Date Range           | 1343-1500 AH | 1356-1500 AH |
| Python 3 Support     |     Full     |   Limited    |
| Rich Comparison      |     Yes      |      No      |
| Input Validation     |     Yes      |      No      |
| Hashable Objects     |     Yes      |      No      |
| Type Annotations     |     Yes      |      No      |
| Test Coverage        |     100%     |      0%      |
| Internationalization | 4 languages  |     None     |
