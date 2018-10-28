from hijriconverter import helper, ummalqura
from typing import Tuple
import datetime
import bisect


class Hijri:
    """
    Hijri(year, month and day)
    A Hijri object represents a Hijri date (year, month and day) in lunar
    or solar Hijri calendar.
    """
    def __init__(self, year: int, month: int, day: int,
                 calendar: str = 'lunar', validated: bool = False) -> None:
        """
        Instantiate Hijri object.
        The year, month and day arguments are required and must be integers.
        The calendar argument is optional and must be a string. It may be
        'lunar' or 'solar'. Default is 'lunar'.
        The validated argument is optional and must be boolean. Default is
        False. When True, it means date is already validated and validation
        will be skipped.
        """
        if not validated:
            helper.validate_hijri_date(year, month, day, calendar)
        self._year = year
        self._month = month
        self._day = day
        self._calendar = calendar

    def __repr__(self) -> str:
        """Return a string representation of the Hijri object."""
        class_name = self.__class__.__name__
        return '{}({}, {}, {}, {})'.format(class_name,
                                           self._year, self._month, self._day,
                                           self._calendar)

    def isoformat(self) -> str:
        """Return a string representing the date in ISO format ‘YYYY-MM-DD’."""
        return '{:04}-{:02}-{:02}'.format(self._year, self._month, self._day)

    __str__ = isoformat

    @property
    def year(self) -> int:
        """Return year as an integer"""
        return self._year

    @property
    def month(self) -> int:
        """Return month as an integer"""
        return self._month

    @property
    def day(self) -> int:
        """Return day as an integer"""
        return self._day

    def datetuple(self) -> Tuple[int, int, int]:
        """Return date as a tuple of (year, month, day)."""
        return self._year, self._month, self._day

    def month_days(self) -> int:
        """Return number of days in month as an integer."""
        return helper.hijri_month_days(self._year, self._month, self._calendar)

    def month_name(self, language: str = 'en') -> str:
        """
        Return month name as a string in specified language.
        The language argument is optional and must be a string. It may
        be 'en' for English or 'ar' for Arabic. Default is 'en'.
        """
        return ummalqura.month_names[self._calendar][language][self._month]

    def weekday(self) -> int:
        """Return day of week as an integer, where Mon is 0 and Sun is 6."""
        jd = helper.hijri_to_julian(self._year, self._month, self._day,
                                    self._calendar)
        return int(jd % 7)

    def isoweekday(self) -> int:
        """Return day of week as an integer, where Mon is 1 and Sun is 7."""
        jd = helper.hijri_to_julian(self._year, self._month, self._day,
                                    self._calendar)
        return int(jd % 7) + 1

    def day_name(self, language: str = 'en') -> str:
        """
        Return day name as a string in specified language.
        The language argument is optional and must be a string. It may
        be 'en' for English or 'ar' for Arabic. Default is 'en'.
        """
        return ummalqura.day_names[language][self.weekday()]

    def to_gregorian(self) -> datetime.date:
        """Return a converted gregorian date as a datetime.date object."""
        jd = helper.hijri_to_julian(self._year, self._month, self._day,
                                    self._calendar)
        gregorian = helper.julian_to_gregorian(jd)
        return datetime.date(*gregorian)


class Gregorian:
    """
    Gregorian(year, month, day)
    A Gregorian object represents a Gregorian date (year, month and day) in
    Gregorian calendar.
    """
    def __init__(self, year: int, month: int, day: int) -> None:
        """
        Instantiate Gregorian object.
        The year, month and day arguments are required and must be integers.
        """
        helper.validate_gregorian_date(year, month, day)
        self._year = year
        self._month = month
        self._day = day

    def __repr__(self) -> str:
        """Return a string representation of the Gregorian object."""
        class_name = self.__class__.__name__
        return '{}({}, {}, {})'.format(class_name,
                                       self._year, self._month, self._day)

    def to_hijri(self, calendar: str = 'lunar') -> Hijri:
        """
        Return a converted hijri date as a Hijri object.
        The calendar argument is optional and must be a string. It may
        be 'lunar' or 'solar'. Default is 'lunar'.
        """
        helper._check_hijri_calendar(calendar)
        jd = helper.gregorian_to_julian(self._year, self._month, self._day)
        mjd = helper.julian_to_modified_julian(jd)
        month_starts = ummalqura.month_starts[calendar]
        i = bisect.bisect_right(month_starts, mjd)
        months = i + ummalqura.first_month_offset[calendar]
        years = int((months - 1) / 12)
        year = years + 1
        month = months - 12 * years
        day = mjd - month_starts[i - 1] + 1
        return Hijri(year, month, day, calendar, validated=True)
