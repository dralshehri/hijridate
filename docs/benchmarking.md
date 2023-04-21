---
hide-toc: true
---

# Benchmarking

Similar Python converters have been mainly derived from or using the [ummalqura]
package developed by Khalid Al-hussayen and updated lately by Borni DHIFI, which
was ported from [hijri.js], a Javascript tool published by Suhail Alkowaileet.
The last goes back to [R.H. van Gent], who built the original converter partly
based on his astronomical calculations for years after 1420 AH and partly on a
comparison calendar prepared by King Fahd University of Petroleum and Minerals
(KFUPM) in 1993 for the years 1356-1411 AH.

In contrast, the **hijri-converter** package was written in Python from scratch.
Although it was inspired by R.H. van Gent's work, it is based on multiple
official sources including archived issues of Umm al-Qura newspaper published
weekly since 1343 AH, one that is in complete alignment with the official
printed Umm al-Qura calendar. Other sources were also used to build the package
including the Comparison Calendar prepared by KFUPM for the years 1356-1411 AH,
the Umm al-Qura Comparative Calendar (Taqwīm Umm al-Qurá al-muqāran) books for
the years 1412-1450 AH, and the official website of Umm al-Qura calendar for the
years 1451-1500 AH. That makes **hijri-converter** package more accurate and
broader in terms of years included, 1343-1500 AH.

When it comes to performance, using **hijri-converter** package to convert from
Hijri to Gregorian and back is about nine times faster (or six times faster,
with Hijri date validation enabled) than that when _ummalqura_ package was used.

```shell
# hijri-converter, without Hijri date validation
$ python -m timeit -s 'from hijri_converter import convert' -n 50000 -r 5 'convert.Hijri(1402, 10, 15, False).to_gregorian(); convert.Gregorian(1982, 8, 4).to_hijri()'
50000 loops, best of 5: 1.69 usec per loop

# hijri-converter, with Hijri date validation
$ python -m timeit -s 'from hijri_converter import convert' -n 50000 -r 5 'convert.Hijri(1402, 10, 15, True).to_gregorian(); convert.Gregorian(1982, 8, 4).to_hijri()'
50000 loops, best of 5: 2.37 usec per loop

# ummalqura, without Hijri date validation
$ python -m timeit -s 'from ummalqura.hijri import Umalqurra' -n 50000 -r 5 'Umalqurra().hijri_to_gregorian(1402, 10, 15); Umalqurra().gegorean_to_hijri(1982, 8, 4)'
50000 loops, best of 5: 13.9 usec per loop
```

The above code illustrates the execution time of both packages compared _(tested
using Python 3.11 on Mac mini (M1, 2020) with Apple M1 chip and 16GB memory)_.

Beside code quality, packaging and maintenance issues that _ummalqura_ package
has, the following table summarizes the main differences:

| Item             | hijri-converter |  ummalqura   |
| :--------------- | :-------------: | :----------: |
| Conversion range |  1343-1500 AH   | 1356-1500 AH |
| Accuracy [^a]    |      100%       |    91.6%     |
| Performance [^p] |  ~9x (faster)   |      1x      |
| Python 3 support |      Full       |   Limited    |
| Rich comparison  |       Yes       |      No      |
| Input validation |       Yes       |      No      |
| Hashable objects |       Yes       |      No      |
| Type annotations |       Yes       |      No      |
| Code testing     |      100%       |     None     |

<!-- prettier-ignore -->
[^a]: Verified with the years 1343-1355 AH included, which are missing from
_ummalqura_ package but can produce wrong dates when used.

<!-- prettier-ignore -->
[^p]: Although not recommended for production, Hijri date validation was
disabled in **hijri-converter** package; to be comparable with _ummalqura_
package.

[ummalqura]: https://pypi.org/project/ummalqura/
[hijri.js]: https://github.com/xsoh/Hijri.js
[r.h. van gent]: http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm
