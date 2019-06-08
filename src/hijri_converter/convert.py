import datetime
from bisect import bisect
from hijri_converter import ummalqura, locales


class Hijri:
    """A Hijri object represents a date (year, month and day) in Hijri
    calendar.
    """

    __slots__ = "_year", "_month", "_day"

    def __init__(self, year: int, month: int, day: int, validate: bool = True) -> None:
        """
        :param year: Hijri year
        :type year: int
        :param month: Hijri month
        :type month: int
        :param day: Hijri day
        :type day: int
        :param validate: Whether to validate date or not (default is ``True``)
        :type validate: bool
        """

        if validate:
            _check_hijri_date(year, month, day)
        self._year = year
        self._month = month
        self._day = day

    def __repr__(self) -> str:
        return f"Hijri({self._year}, {self._month}, {self._day})"

    def __str__(self) -> str:
        return self.isoformat()

    def __hash__(self) -> int:
        return hash(("Hijri", self._year, self._month, self._day))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            return False
        return self._compare(other) == 0

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            self._compare_error(other)
        return self._compare(other) > 0

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            self._compare_error(other)
        return self._compare(other) >= 0

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            self._compare_error(other)
        return self._compare(other) < 0

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            self._compare_error(other)
        return self._compare(other) <= 0

    def _compare(self, other: "Hijri") -> int:
        x = self.datetuple()
        y = other.datetuple()
        return 0 if x == y else 1 if x > y else -1

    def _compare_error(self, other: object) -> None:
        """Raise an error when comparing Hijri object to non-Hijri object."""
        raise TypeError(f"can't compare 'Hijri' to '{type(other).__name__}'")

    @classmethod
    def fromisoformat(cls, date_string: str):
        """Construct Hijri object from an ISO formatted Hijri date
        'YYYY-MM-DD'.

        :param date_string: Hijri date in ISO format ``YYYY-MM-DD``
        :type date_string: str
        :return: Hijri date object
        :rtype: Hijri
        """

        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        return cls(year, month, day)

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
        return f"{self._year:04}-{self._month:02}-{self._day:02}"

    def slashformat(self) -> str:
        """Return Hijri date in slash format 'DD/MM/YYYY'."""
        return f"{self._day:02}/{self._month:02}/{self._year:04}"

    def month_length(self) -> int:
        """Return number of days in Hijri month."""
        month_index = _hijri_month_index(self._year, self._month)
        month_length = _hijri_month_length(month_index)
        return month_length

    def month_name(self, language: str = "en") -> str:
        """Return Hijri month name.

        :param language: Language for localized translation which may be
            ``en`` or ``ar`` (default is ``en``)
        :type language: str
        """

        return getattr(locales, language).hijri_months[self._month]

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

        :param language: Language for localized translation which may be
            ``en`` or ``ar`` (default is ``en``)
        :type language: str
        """

        return getattr(locales, language).weekday_names[self.weekday()]

    @staticmethod
    def notation(language: str = "en") -> str:
        """Return calendar notation/abbreviation.

        :param language: Language for localized translation which may be
            ``en`` or ``ar`` (default is ``en``)
        :type language: str
        """

        return getattr(locales, language).hijri_notation

    def to_julian(self) -> int:
        """Convert Hijri date to Julian Day (JD) number."""
        month_starts = ummalqura.month_starts
        index = _hijri_month_index(self._year, self._month)
        rjd = month_starts[index] + self._day - 1
        jd = _reduced_julian_to_julian(rjd)
        return jd

    def to_gregorian(self) -> "Gregorian":
        """Convert Hijri date to Gregorian date.

        :return: Gregorian date object
        :rtype: Gregorian
        """

        jd = self.to_julian()
        return Gregorian.fromordinal(_julian_to_ordinal(jd))


class Gregorian(datetime.date):
    """A Gregorian object represents a date (year, month and day) in Gregorian
    calendar inheriting all attributes and methods of `datetime.date` object.
    """

    __slots__ = ()

    @classmethod
    def fromdate(cls, date_object: datetime.date) -> "Gregorian":
        """Construct Gregorian object from a date object.

        :param date_object: Date object
        :type date_object: datetime.date
        :return: Gregorian date object
        :rtype: Gregorian
        """

        year, month, day = date_object.timetuple()[:3]
        return cls(year, month, day)

    def datetuple(self) -> tuple:
        """Return Gregorian date as a tuple of (year, month, day)."""
        return self.year, self.month, self.day

    def slashformat(self) -> str:
        """Return Hijri date in slash format 'DD/MM/YYYY'."""
        return f"{self.day:02}/{self.month:02}/{self.year:04}"

    def month_name(self, language: str = "en") -> str:
        """Return Hijri month name.

        :param language: Language for localized translation which may be
            ``en`` or ``ar`` (default is ``en``)
        :type language: str
        """

        return getattr(locales, language).gregorian_months[self.month]

    def day_name(self, language: str = "en") -> str:
        """Return day name.

        :param language: Language for localized translation which may be
            ``en`` or ``ar`` (default is ``en``)
        :type language: str
        """

        return getattr(locales, language).weekday_names[self.weekday()]

    @staticmethod
    def notation(language: str = "en") -> str:
        """Return calendar notation/abbreviation.

        :param language: Language for localized translation which may be
            ``en`` or ``ar`` (default is ``en``)
        :type language: str
        """

        return getattr(locales, language).gregorian_notation

    def to_julian(self) -> int:
        """Convert Gregorian date to Julian Day (JD) number."""
        jd = _ordinal_to_julian(self.toordinal())
        return jd

    def to_hijri(self) -> Hijri:
        """Convert Gregorian date to Hijri date.

        :return: Hijri date object
        :rtype: Hijri
        """

        _check_gregorian_range(self.year, self.month, self.day)
        jd = self.to_julian()
        rjd = _julian_to_reduced_julian(jd)
        month_starts = ummalqura.month_starts
        index = bisect(month_starts, rjd) - 1
        months = index + ummalqura.hijri_offset
        years = int(months / 12)
        year = years + 1
        month = months - (years * 12) + 1
        day = rjd - month_starts[index] + 1
        return Hijri(year, month, day, validate=False)


def _check_gregorian_range(year: int, month: int, day: int) -> None:
    """Check if Gregorian date is within valid conversion range."""
    min_date, max_date = ummalqura.gregorian_range
    if not min_date <= (year, month, day) <= max_date:
        raise OverflowError("date out of range")


def _check_hijri_date(year: int, month: int, day: int) -> None:
    """Check Hijri date values and if date is within valid conversion range."""
    # check year
    min_year, max_year = [d[0] for d in ummalqura.hijri_range]
    if not min_year <= year <= max_year:
        raise OverflowError("date out of range")
    # check month
    if not 1 <= month <= 12:
        raise ValueError("month must be in 1..12")
    # check day
    month_index = _hijri_month_index(year, month)
    month_length = _hijri_month_length(month_index)
    if not 1 <= day <= month_length:
        raise ValueError(f"day must be in 1..{month_length} for month")


def _hijri_month_index(year: int, month: int) -> int:
    """Return index of month in Hijri month starts."""
    months = ((year - 1) * 12) + month - 1
    index = months - ummalqura.hijri_offset
    return index


def _hijri_month_length(index: int) -> int:
    """Return number of days in Hijri month."""
    month_starts = ummalqura.month_starts
    length = month_starts[index + 1] - month_starts[index]
    return length


def _julian_to_ordinal(jd: int) -> int:
    """Convert Julian Day (JD) number to ordinal number."""
    return jd - 1721425


def _ordinal_to_julian(n: int) -> int:
    """Convert ordinal number to Julian Day (JD) number."""
    return n + 1721425


def _julian_to_reduced_julian(jd: int) -> int:
    """Convert Julian Day (JD) number to Reduced Julian Day (RJD) number."""
    return jd - 2400000


def _reduced_julian_to_julian(rjd: int) -> int:
    """Convert Reduced Julian Day (RJD) number to Julian Day (JD) number."""
    return rjd + 2400000
