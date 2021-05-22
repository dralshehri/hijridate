---
hide-toc: true
---

# Benchmarking

Similar Python converters have been mainly derived from or using the
[Umalqurra] package by Khalid Al-hussayen, which was ported from [Hijri.js],
a Javascript tool published by Suhail Alkowaileet. The last goes back to
[R.H. van Gent], who built the original converter partly based on his
astronomical calculation for years after 1420 AH and partly on a comparison
calendar prepared by KFUPM in 1993 for the years 1356-1411 AH.

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
Hijri to Gregorian and back is seven times faster (or five times faster, with
Hijri date validation enabled) than that when [Umalqurra] package was used.

```shell
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
```

The above code illustrates the execution time of both packages compared
*(tested on Macbook Pro with 2.9GHz Intel Core i5 processor and 16GB memory)*.

Beside packaging and maintenance issues that [Umalqurra] package
has, the following table summarizes the main differences:

| Item                  | Hijri Converter | Umalqurra     |
| :--------------------- | :-------------: | :-----------: |
| Years included        | 1343-1500 AH    | 1356-1500 AH  |
| Accuracy [^1]         | 100%            | 91.6%         |
| Performance [^2]      | 7x (faster)     | 1x            |
| Python 3 support      | Full            | Limited       |
| Dates rich comparison | Yes             | No            |
| Hijri date validation | Yes             | No            |
| Code testing          | Yes             | No            |


[^1]: Verified with the years 1343-1355 AH included, which are missing from 
[Umalqurra] package but can produce wrong dates when used.

[^2]: Hijri date validation was disabled in *Hijri Converter* package;
to be comparable with [Umalqurra] package.

[Hijri Converter]: https://pypi.org/project/hijri-converter/
[Umalqurra]: https://pypi.org/project/umalqurra/
[Hijri.js]: https://github.com/xsoh/Hijri.js
[R.H. van Gent]: http://www.staff.science.uu.nl/~gent0113/islam/ummalqura.htm
