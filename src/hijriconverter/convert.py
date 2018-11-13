from hijriconverter import helper, ummalqura
from typing import Tuple
from datetime import date
import bisect


class Hijri:
    """A Hijri object represents a Hijri date (year, month and day) in lunar
    or solar Hijri calendar.
    """

    def __init__(self, year: int, month: int, day: int,
                 calendar: str = 'lunar') -> None:
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
        """

        calendar = helper.check_hijri_calendar(calendar)
        year, month, day = helper.check_date(year, month, day, calendar)
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
        return helper.hijri_month_days(self._year, self._month, self._calendar)

    def month_name(self, language: str = 'en') -> str:
        """Return Hijri month name.

        :param language: language which may be 'en' or 'ar'
            (default is ``en``)
        :type language: str
        """

        return ummalqura.months[language][self._calendar][self._month]

    def weekday(self) -> int:
        """Return day of week, where Monday is 0 ... Sunday is 6."""
        jd = helper.hijri_to_julian(self._year, self._month, self._day,
                                    self._calendar)
        return int(jd % 7)

    def isoweekday(self) -> int:
        """Return day of week, where Monday is 1 ... Sunday is 7."""
        jd = helper.hijri_to_julian(self._year, self._month, self._day,
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

        jd = helper.hijri_to_julian(self._year, self._month, self._day,
                                    self._calendar)
        gregorian = helper.julian_to_gregorian(jd)
        return date(*gregorian)


class Gregorian:
    """A Gregorian object represents a Gregorian date (year, month and day) in
    Gregorian calendar.
    """

    def __init__(self, year: int, month: int, day: int) -> None:
        """
        :param year: Gregorian year
        :type year: int
        :param month: Gregorian month
        :type month: int
        :param day: Gregorian day
        :type day: int
        """

        year, month, day = helper.check_date(year, month, day, 'gregorian')
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

        calendar = helper.check_hijri_calendar(calendar)
        jd = helper.gregorian_to_julian(self._year, self._month, self._day)
        mjd = helper.julian_to_modified_julian(jd)
        month_starts = ummalqura.starts[calendar]
        i = bisect.bisect_right(month_starts, mjd)
        months = i + ummalqura.offset[calendar]
        years = int((months - 1) / 12)
        year = years + 1
        month = months - 12 * years
        day = mjd - month_starts[i - 1] + 1
        return Hijri(year, month, day, calendar)
