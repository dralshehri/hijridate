from hijriconverter import ummalqura
from typing import Tuple
from datetime import date
import bisect


class Hijri:
    """A Hijri object represents a Hijri date (year, month and day) in lunar
    or solar Hijri calendar.
    """

    def __init__(self, year: int, month: int, day: int,
                 calendar: str = 'lunar', validate: bool = False) -> None:
        """
        :param year: Hijri year
        :type year: int
        :param month: Hijri month
        :type month: int
        :param day: Hijri day
        :type day: int
        :param calendar: Hijri calendar which may be ``lunar`` or ``solar``
            (default is ``lunar``)
        :type calendar: str
        :param validate: check date values and if date is within valid
            conversion range (default is ``False``)
        :type validate: bool
        """

        if validate:
            year, month, day, calendar = _check_date(year, month, day,
                                                     calendar)
        self._year = year
        self._month = month
        self._day = day
        self._calendar = calendar

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return '{}({}, {}, {}, {})'.format(class_name,
                                           self._year, self._month, self._day,
                                           self._calendar)

    def __str__(self) -> str:
        return self.isoformat()

    @property
    def year(self) -> int:
        """Return Hijri year as an integer."""
        return self._year

    @property
    def month(self) -> int:
        """Return Hijri month as an integer."""
        return self._month

    @property
    def day(self) -> int:
        """Return Hijri day as an integer."""
        return self._day

    def datetuple(self) -> Tuple[int, int, int]:
        """Return Hijri date as a tuple of (year, month, day)."""
        return self._year, self._month, self._day

    def isoformat(self) -> str:
        """Return Hijri date in ISO format 'YYYY-MM-DD'."""
        return '{:04}-{:02}-{:02}'.format(self._year, self._month, self._day)

    def slashformat(self) -> str:
        """Return Hijri date in slash format 'DD/MM/YYYY'."""
        return '{:02}/{:02}/{:04}'.format(self._day, self._month, self._year)

    def month_days(self) -> int:
        """Return number of days in Hijri month."""
        return _hijri_month_days(self._year, self._month, self._calendar)

    def month_name(self, language: str = 'en') -> str:
        """Return Hijri month name.

        :param language: language which may be 'en' or 'ar'
            (default is ``en``)
        :type language: str
        """

        return ummalqura.months[language][self._calendar][self._month]

    def weekday(self) -> int:
        """Return day of week, where Monday is 0 ... Sunday is 6."""
        jd = _hijri_to_julian(self._year, self._month, self._day,
                              self._calendar)
        return int(jd % 7)

    def isoweekday(self) -> int:
        """Return day of week, where Monday is 1 ... Sunday is 7."""
        jd = _hijri_to_julian(self._year, self._month, self._day,
                              self._calendar)
        return int(jd % 7) + 1

    def day_name(self, language: str = 'en') -> str:
        """Return day name.

        :param language: language which may be ``en`` or ``ar``
            (default is 'en')
        :type language: str
        """

        return ummalqura.days[language][self.weekday()]

    def to_gregorian(self) -> date:
        """Convert Hijri date to Gregorian date.

        :return: Gregorian date object
        :rtype: datetime.date
        """

        jd = _hijri_to_julian(self._year, self._month, self._day,
                              self._calendar)
        gregorian = _julian_to_gregorian(jd)
        return date(*gregorian)


class Gregorian:
    """A Gregorian object represents a Gregorian date (year, month and day) in
    Gregorian calendar.
    """

    def __init__(self, year: int, month: int, day: int,
                 validate: bool = False) -> None:
        """
        :param year: Gregorian year
        :type year: int
        :param month: Gregorian month
        :type month: int
        :param day: Gregorian day
        :type day: int
        :param validate: check date values and if date is within valid
            conversion range (default is ``False``)
        :type validate: bool
        """

        if validate:
            year, month, day = _check_date(year, month, day)[:3]
        self._year = year
        self._month = month
        self._day = day

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return '{}({}, {}, {})'.format(class_name,
                                       self._year, self._month, self._day)

    def to_hijri(self, calendar: str = 'lunar') -> Hijri:
        """Convert Gregorian date to Hijri date.

        :param calendar: Hijri calendar which may be ``lunar`` or ``solar``
            (default is ``lunar``)
        :type calendar: str
        :return: Hijri date object
        :rtype: Hijri
        """

        jd = _gregorian_to_julian(self._year, self._month, self._day)
        mjd = _julian_to_modified_julian(jd)
        month_starts = ummalqura.starts[calendar]
        i = bisect.bisect_right(month_starts, mjd)
        months = i + ummalqura.offset[calendar]
        years = int((months - 1) / 12)
        year = years + 1
        month = months - 12 * years
        day = mjd - month_starts[i - 1] + 1
        return Hijri(year, month, day, calendar)


def _check_date(year: int, month: int, day: int,
                calendar: str = 'gregorian') -> Tuple[int, int, int, str]:
    """Check date values and if it's within conversion range."""
    # check calendar
    if not isinstance(calendar, str):
        raise TypeError('calendar must be a string')
    calendar = calendar.lower()
    hijri_calendars = ['lunar', 'solar']
    if calendar != 'gregorian' and calendar not in hijri_calendars:
        raise ValueError('calendar must be \'{}\' or \'{}\''.format(
                *hijri_calendars))
    # check year
    if not isinstance(year, int):
        raise TypeError('year must be an integer')
    if year < 1 or len(str(year)) != 4:
        raise ValueError('year must be in yyyy format')
    # check month
    if not isinstance(month, int):
        raise TypeError('month must be an integer')
    if not 1 <= month <= 12:
        raise ValueError('month must be in 1..12')
    # check range
    calendar_range = ummalqura.ranges[calendar]
    if not calendar_range[0] <= (year, month, day) <= calendar_range[1]:
        raise ValueError('date is out of range for conversion')
    # check day
    if not isinstance(day, int):
        raise TypeError('day must be an integer')
    if calendar == 'gregorian':
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        gregorian_months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and is_leap:
            month_days = 29
        else:
            month_days = gregorian_months[month]
    else:
        month_days = _hijri_month_days(year, month, calendar)
    if not 1 <= day <= month_days:
        raise ValueError('day must be in 1..{} for month'.format(month_days))
    return year, month, day, calendar


def _hijri_month_index(year: int, month: int, calendar: str) -> int:
    """Return index of month's modified Julian day in ummalqura ``starts``."""
    years = year - 1
    months = (years * 12) + month
    index = months - ummalqura.offset[calendar]
    return index


def _hijri_month_days(year: int, month: int, calendar: str) -> int:
    """Return number of days in Hijri month."""
    i = _hijri_month_index(year, month, calendar)
    month_starts = ummalqura.starts[calendar]
    days = month_starts[i] - month_starts[i - 1]
    return days


def _hijri_to_julian(year: int, month: int, day: int, calendar: str) -> int:
    """Convert Hijri date to Julian day."""
    i = _hijri_month_index(year, month, calendar)
    month_starts = ummalqura.starts[calendar]
    mjd = day + month_starts[i - 1] - 1
    jd = _modified_julian_to_julian(mjd)
    return jd


def _gregorian_to_julian(year: int, month: int, day: int) -> int:
    """Convert Gregorian date to Julian day."""
    i = int((month - 14) / 12)
    jd = int((1461 * (year + 4800 + i)) / 4)
    jd += int((367 * (month - 2 - (12 * i))) / 12)
    jd -= int((3 * int((year + 4900 + i) / 100)) / 4)
    jd += day - 32075
    return jd


def _julian_to_gregorian(jd: int) -> Tuple[int, int, int]:
    """Convert Julian day to Gregorian date."""
    i = jd + 68569
    n = int((4 * i) / 146097)
    i -= int(((146097 * n) + 3) / 4)
    ii = int((4000 * (i + 1)) / 1461001)
    i -= int((1461 * ii) / 4) - 31
    j = int((80 * i) / 2447)
    day = i - int((2447 * j) / 80)
    i = int(j / 11)
    month = j + 2 - (12 * i)
    year = 100 * (n - 49) + ii + i
    return year, month, day


def _julian_to_modified_julian(jd: int) -> int:
    """Convert Julian day to modified Julian day number."""
    mjd0 = 2400000
    return jd - mjd0


def _modified_julian_to_julian(mjd: int) -> int:
    """Convert modified Julian day number to Julian day."""
    mjd0 = 2400000
    return mjd + mjd0
