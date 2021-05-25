---
hide-toc: true
---

# Benchmarking

Similar Python converters have been mainly derived from or using the
[Ummalqura] package developed by Khalid Al-hussayen and updated lately by Borni DHIFI,
which was ported from [Hijri.js], a Javascript tool published by Suhail Alkowaileet.
The last goes back to [R.H. van Gent], who built the original converter partly based on
his astronomical calculations for years after 1420 AH and partly on a comparison
calendar prepared by King Fahd University of Petroleum and Minerals (KFUPM) in 1993
for the years 1356-1411 AH.

In contrast, the [Hijri Converter] package was written in Python from scratch.
Although it was inspired by R.H. van Gent's work, it is mainly based on the
Umm al-Qura newspaper issues published weekly since 1343 AH, one that is in
complete alignment with the official printed Umm al-Qura calendar. However,
other sources was also used to build the package including the comparison
calendar prepared by KFUPM for the years 1356-1411 AH, and the official website
of Umm al-Qura calendar for the years 1431-1500 AH. Both sources were also
verified using the dates of then-published issues of Umm al-Qura newspaper.
That makes [Hijri Converter] package more accurate and broader in terms of
years included, 1343-1500 AH.

When it comes to performance, using [Hijri Converter] package to convert from
Hijri to Gregorian and back is nine times faster (or six times faster, with
Hijri date validation enabled) than that when [Ummalqura] package was used.

```shell
# Hijri Converter, without Hijri date validation
$ python -m timeit -s 'from hijri_converter import convert' -n 50000 -r 5 'convert.Hijri(1402, 10, 15, False).to_gregorian(); convert.Gregorian(1982, 8, 4).to_hijri()'
50000 loops, best of 5: 1.84 usec per loop

# Hijri Converter, with Hijri date validation
$ python -m timeit -s 'from hijri_converter import convert' -n 50000 -r 5 'convert.Hijri(1402, 10, 15, True).to_gregorian(); convert.Gregorian(1982, 8, 4).to_hijri()'
50000 loops, best of 5: 2.67 usec per loop

# Ummalqura, without Hijri date validation
$ python -m timeit -s 'from ummalqura.hijri import Umalqurra' -n 50000 -r 5 'Umalqurra().hijri_to_gregorian(1402, 10, 15); Umalqurra().gegorean_to_hijri(1982, 8, 4)'
50000 loops, best of 5: 17.3 usec per loop
```

The above code illustrates the execution time of both packages compared
*(tested on Mac mini (M1, 2020) with Apple M1 chip and 16GB memory)*.

Beside code quality, packaging and maintenance issues that [Ummalqura] package
has, the following table summarizes the main differences:

| Item              | Hijri Converter | Ummalqura     |
| :---------------- | :-------------: | :-----------: |
| Conversion range  | 1343-1500 AH    | 1356-1500 AH  |
| Accuracy [^1]     | 100%            | 91.6%         |
| Performance [^2]  | 9x (faster)     | 1x            |
| Python 3 support  | Full            | Limited       |
| Rich comparison   | Yes             | No            |
| Input validation  | Yes             | No            |
| Hashable objects  | Yes             | No            |
| Type annotations  | Yes             | No            |
| Code testing      | 100%            | None          |


[^1]: Verified with the years 1343-1355 AH included, which are missing from 
[Ummalqura] package but can produce wrong dates when used.

[^2]: Hijri date validation was disabled in [Hijri Converter] package;
to be comparable with [Ummalqura] package.

[Hijri Converter]: https://pypi.org/project/hijri-converter/
[Ummalqura]: https://pypi.org/project/ummalqura/
[Hijri.js]: https://github.com/xsoh/Hijri.js
[R.H. van Gent]: http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm
