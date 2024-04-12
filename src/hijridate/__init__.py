"""Accurate Hijri-Gregorian dates converter based on the Umm al-Qura calendar.

https://github.com/dralshehri/hijridate
"""

from hijridate._version import __version__
from hijridate.convert import Gregorian, Hijri

__all__ = ["__version__", "Gregorian", "Hijri"]
