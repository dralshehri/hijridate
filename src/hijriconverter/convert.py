from hijriconverter import ummalqura
from datetime import date
import bisect


class Hijri:
    """A Hijri object represents a date (year, month and day) in lunar or
    solar Hijri calendar.
    """

    def __new__(
        cls, year: int, month: int, day: int, calendar: str = "lunar"
    ) -> "Hijri":
        """Construct Hijri date object after date validation"""
        _check_hijri_date(year, month, day, calendar)
        return super().__new__(cls)

    def __init__(
        self, year: int, month: int, day: int, calendar: str = "lunar"
    ) -> None:
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

        self._year = year
        self._month = month
        self._day = day
        self._calendar = calendar.lower()
        self._calendar_class = getattr(ummalqura, calendar.title())
        self._index = _hijri_month_index(year, month, self._calendar_class)

    def __repr__(self) -> str:
        return "Hijri({}, {}, {}, {})".format(
            self._year, self._month, self._day, self._calendar
        )

    def __str__(self) -> str:
        return self.isoformat()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            raise TypeError("second operand must be 'Hijri' object")
        return self.datetuple() == other.datetuple()

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            raise TypeError("second operand must be 'Hijri' object")
        return self.datetuple() > other.datetuple()

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            raise TypeError("second operand must be 'Hijri' object")
        return self.datetuple() >= other.datetuple()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            raise TypeError("second operand must be 'Hijri' object")
        return self.datetuple() < other.datetuple()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            raise TypeError("second operand must be 'Hijri' object")
        return self.datetuple() <= other.datetuple()

    @classmethod
    def fromisoformat(cls, date_string: str, calendar: str = "lunar"):
        """Construct Hijri object from an ISO formatted Hijri date
        'YYYY-MM-DD'.

        :param date_string: Hijri date in ISO format ``YYYY-MM-DD``
        :type date_string: str
        :param calendar: Hijri calendar which may be ``lunar`` or ``solar``
            (default is ``lunar``)
        :type calendar: str

        """

        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        return cls(year, month, day, calendar)

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

    def datetuple(self) -> tuple:
        """Return Hijri date as a tuple of (year, month, day)."""
        return self._year, self._month, self._day

    def isoformat(self) -> str:
        """Return Hijri date in ISO format 'YYYY-MM-DD'."""
        return "{:04}-{:02}-{:02}".format(self._year, self._month, self._day)

    def slashformat(self) -> str:
        """Return Hijri date in slash format 'DD/MM/YYYY'."""
        return "{:02}/{:02}/{:04}".format(self._day, self._month, self._year)

    def month_days(self) -> int:
        """Return number of days in Hijri month."""
        return _hijri_month_days(self._index, self._calendar_class)

    def month_name(self, language: str = "en") -> str:
        """Return Hijri month name.

        :param language: language which may be ``en`` or ``ar``
            (default is ``en``)
        :type language: str
        """

        return self._calendar_class.month_names[language][self._month]

    def weekday(self) -> int:
        """Return day of week, where Monday is 0 ... Sunday is 6."""
        jd = self.to_julian()
        return int(jd % 7)

    def isoweekday(self) -> int:
        """Return day of week, where Monday is 1 ... Sunday is 7."""
        jd = self.to_julian()
        return int(jd % 7) + 1

    def day_name(self, language: str = "en") -> str:
        """Return day name.

        :param language: language which may be ``en`` or ``ar``
            (default is ``en``)
        :type language: str
        """

        return ummalqura.day_names[language][self.weekday()]

    def notation(self, language: str = "en") -> str:
        """Return calendar notation.

        :param language: language which may be ``en`` or ``ar``
            (default is ``en``)
        :type language: str
        """

        return self._calendar_class.notations[language]

    def to_julian(self) -> int:
        """Convert Hijri date to Julian day number."""
        month_starts = self._calendar_class.month_starts
        rjd = self._day + month_starts[self._index - 1] - 1
        jd = _reduced_julian_to_julian(rjd)
        return jd

    def to_gregorian(self) -> "Gregorian":
        """Convert Hijri date to Gregorian date.

        :return: Gregorian date object
        :rtype: Gregorian
        """

        jd = self.to_julian()
        rd = _julian_to_ordinal(jd)
        return Gregorian.fromordinal(rd)


class Gregorian(date):
    """A Gregorian object represents a date (year, month and day) in Gregorian
    calendar inheriting all attributes and methods of `datetime.date` object.
    """

    @classmethod
    def fromdate(cls, date_object: date) -> "Gregorian":
        """Construct Gregorian object from a date object.

        :param date_object: Date object
        :type date_object: datetime.date
        """

        year, month, day = date_object.timetuple()[:3]
        return cls(year, month, day)

    def to_hijri(self, calendar: str = "lunar") -> Hijri:
        """Convert Gregorian date to Hijri date.

        :param calendar: Hijri calendar which may be ``lunar`` or ``solar``
            (default is ``lunar``)
        :type calendar: str
        :return: Hijri date object
        :rtype: Hijri
        """

        self._check_range()
        calendar_class = getattr(ummalqura, calendar.title())
        jd = _ordinal_to_julian(self.toordinal())
        rjd = _julian_to_reduced_julian(jd)
        month_starts = calendar_class.month_starts
        index = bisect.bisect_right(month_starts, rjd)
        months = index + calendar_class.first_offset
        years = int((months - 1) / 12)
        year = years + 1
        month = months - 12 * years
        day = rjd - month_starts[index - 1] + 1
        return _ValidatedHijri(year, month, day, calendar)

    def _check_range(self) -> None:
        """Check if date is within valid conversion range."""
        range_ = (1937, 3, 14), (2077, 11, 16)  # including end
        if not range_[0] <= (self.year, self.month, self.day) <= range_[1]:
            raise OverflowError("date is out of range for conversion")


class _ValidatedHijri(Hijri):
    """A Hijri object converted from Gregorian date. This implementation is
    to avoid double checking of date.
    """

    def __new__(cls, *args, **kwargs) -> "Hijri":
        return super(Hijri, cls).__new__(cls)


def _check_hijri_date(year: int, month: int, day: int, calendar: str) -> None:
    """Check Hijri date values and if date is within valid conversion range."""
    # check calendar
    calendar = calendar.lower()
    calendars = ["lunar", "solar"]
    if calendar not in calendars:
        raise ValueError("calendar must be '{}' or '{}'".format(*calendars))
    calendar_class = getattr(ummalqura, calendar.title())
    # check year
    if len(str(year)) != 4:
        raise ValueError("year must be in yyyy format")
    # check month
    if not 1 <= month <= 12:
        raise ValueError("month must be in 1..12")
    # check range
    valid_range = calendar_class.valid_range
    if not valid_range[0] <= (year, month, day) <= valid_range[1]:
        raise OverflowError("date is out of range for conversion")
    # check day
    month_index = _hijri_month_index(year, month, calendar_class)
    month_days = _hijri_month_days(month_index, calendar_class)
    if not 1 <= day <= month_days:
        raise ValueError("day must be in 1..{} for month".format(month_days))


def _hijri_month_index(year: int, month: int, calendar_class) -> int:
    """Return index of month in Hijri month starts."""
    months = ((year - 1) * 12) + month
    index = months - calendar_class.first_offset
    return index


def _hijri_month_days(index: int, calendar_class) -> int:
    """Return number of days in Hijri month."""
    month_starts = calendar_class.month_starts
    days = month_starts[index] - month_starts[index - 1]
    return days


def _julian_to_ordinal(jd: int) -> int:
    """Convert Julian day number to ordinal number."""
    return jd - 1721425


def _ordinal_to_julian(rd: int) -> int:
    """Convert ordinal number to Julian day number."""
    return rd + 1721425


def _julian_to_reduced_julian(jd: int) -> int:
    """Convert Julian day number to reduced Julian day number."""
    return jd - 2400000


def _reduced_julian_to_julian(rjd: int) -> int:
    """Convert reduced Julian day number to Julian day number."""
    return rjd + 2400000


def _gregorian_to_julian(year: int, month: int, day: int) -> int:
    """Convert Gregorian date to Julian day number. (NOT USED)"""
    i = int((month - 14) / 12)
    jd = int((1461 * (year + 4800 + i)) / 4)
    jd += int((367 * (month - 2 - (12 * i))) / 12)
    jd -= int((3 * int((year + 4900 + i) / 100)) / 4)
    jd += day - 32075
    return jd


def _julian_to_gregorian(jd: int) -> tuple:
    """Convert Julian day number to Gregorian date. (NOT USED)"""
    i = jd + 68569
    n = int((4 * i) / 146097)
    i -= int(((146097 * n) + 3) / 4)
    year = int((4000 * (i + 1)) / 1461001)
    i -= int((1461 * year) / 4) - 31
    month = int((80 * i) / 2447)
    day = i - int((2447 * month) / 80)
    i = int(month / 11)
    month += 2 - (12 * i)
    year += 100 * (n - 49) + i
    return year, month, day
