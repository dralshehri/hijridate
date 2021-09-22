"""Main module of the hijri-converter package."""

import datetime
from bisect import bisect

from hijri_converter import helpers, locales, ummalqura


class Hijri:
    """A Hijri object represents a date (year, month and day) in Hijri calendar."""

    __slots__ = "_year", "_month", "_day"

    def __init__(self, year: int, month: int, day: int, validate: bool = True):
        """
        :param year: Hijri year.
        :type year: int
        :param month: Hijri month.
        :type month: int
        :param day: Hijri day.
        :type day: int
        :param validate: Whether to validate Hijri input or not. It's recommended to
            keep the default for accurate conversion.
        :type validate: bool
        """

        self._year = year
        self._month = month
        self._day = day

        if validate:
            self._check_date()

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}({self._year}, {self._month}, {self._day})"

    def __str__(self) -> str:
        return self.isoformat()

    def __hash__(self) -> int:
        return hash(("Hijri", self._year, self._month, self._day))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            return NotImplemented
        return self._compare(other) == 0

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            return NotImplemented
        return self._compare(other) > 0

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            return NotImplemented
        return self._compare(other) >= 0

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            return NotImplemented
        return self._compare(other) < 0

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Hijri):
            return NotImplemented
        return self._compare(other) <= 0

    def _compare(self, other: "Hijri") -> int:
        x = self.datetuple()
        y = other.datetuple()
        return 0 if x == y else 1 if x > y else -1

    @classmethod
    def fromisoformat(cls, date_string: str) -> "Hijri":
        """Construct Hijri object from an ISO formatted Hijri date
        ``YYYY-MM-DD``.

        :param date_string: Hijri date in ISO format ``YYYY-MM-DD``.
        :type date_string: str
        :rtype: Hijri
        """

        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        return cls(year, month, day)

    @classmethod
    def today(cls) -> "Hijri":
        """Construct Hijri object from today's date.

        :rtype: Hijri
        """
        return Gregorian.today().to_hijri()

    @property
    def year(self) -> int:
        """Return year as an integer."""
        return self._year

    @property
    def month(self) -> int:
        """Return month as an integer."""
        return self._month

    @property
    def day(self) -> int:
        """Return day as an integer."""
        return self._day

    def datetuple(self) -> tuple:
        """Return date as a tuple of (year, month, day)."""
        return self._year, self._month, self._day

    def isoformat(self) -> str:
        """Return date in ISO format i.e. ``YYYY-MM-DD``."""
        return f"{self._year:04}-{self._month:02}-{self._day:02}"

    def dmyformat(self, separator: str = "/", padding: bool = True) -> str:
        """Return date in day-month-year format (``DD/MM/YYYY`` by default).

        :param separator: String that separates the day, month, and year values.
        :type separator: str
        :param padding: Whether to add a leading zero as a padding character to fill
            day and month values when less than 10.
        :type padding: bool
        """

        day = f"{self._day:02}" if padding else self._day
        month = f"{self._month:02}" if padding else self._month
        return f"{day}{separator}{month}{separator}{self._year}"

    def month_length(self) -> int:
        """Return number of days in month."""
        month_starts = ummalqura.MONTH_STARTS
        index = self._month_index()
        length = month_starts[index + 1] - month_starts[index]
        return length

    def month_name(self, language: str = "en") -> str:
        """Return month name.

        :param language: Language tag for localized month name. Full locale name can
            be used, e.g. ``en-US`` or ``en_US.UTF-8``. Supported languages are
            ``en``, ``ar`` and ``bn``.
        :type language: str
        """

        return locales.get_locale(language).month_name(self._month)

    def weekday(self) -> int:
        """Return day of week, where Monday is 0 and Sunday is 6."""
        jdn = self.to_julian()
        return int(jdn % 7)

    def isoweekday(self) -> int:
        """Return day of week, where Monday is 1 and Sunday is 7."""
        jdn = self.to_julian()
        return int(jdn % 7) + 1

    def day_name(self, language: str = "en") -> str:
        """Return day name.

        :param language: Language tag for localized day name. Full locale name can
            be used, e.g. ``en-US`` or ``en_US.UTF-8``. Supported languages are
            ``en``, ``ar`` and ``bn``.
        :type language: str
        """

        return locales.get_locale(language).day_name(self.isoweekday())

    @staticmethod
    def notation(language: str = "en") -> str:
        """Return calendar era notation.

        :param language: Language tag for localized notation. Full locale name can
            be used, e.g. ``en-US`` or ``en_US.UTF-8``. Supported languages are
            ``en``, ``ar`` and ``bn``.
        :type language: str
        """

        return locales.get_locale(language).notation

    def to_julian(self) -> int:
        """Return corresponding Julian day number (JDN)."""
        month_starts = ummalqura.MONTH_STARTS
        index = self._month_index()
        rjd = month_starts[index] + self._day - 1
        jdn = helpers.rjd_to_jdn(rjd)
        return jdn

    def to_gregorian(self) -> "Gregorian":
        """Return Gregorian object for the corresponding Hijri date.

        :rtype: Gregorian
        """

        jdn = self.to_julian()
        n = helpers.jdn_to_ordinal(jdn)
        return Gregorian.fromordinal(n)

    def _check_date(self) -> None:
        """Check date values if within valid range."""
        # check year
        min_year, max_year = [d[0] for d in ummalqura.HIJRI_RANGE]
        if not min_year <= self.year <= max_year:
            raise OverflowError("date out of range")
        # check month
        if not 1 <= self.month <= 12:
            raise ValueError("month must be in 1..12")
        # check day
        month_length = self.month_length()
        if not 1 <= self.day <= month_length:
            raise ValueError(f"day must be in 1..{month_length} for month")

    def _month_index(self) -> int:
        """Return month’s index in ummalqura month starts"""
        prior_months = ((self.year - 1) * 12) + self.month - 1
        index = prior_months - ummalqura.HIJRI_OFFSET
        return index


class Gregorian(datetime.date):
    """A Gregorian object represents a date (year, month and day) in Gregorian
    calendar.
    """

    __slots__ = ()

    @classmethod
    def fromdate(cls, date_object: datetime.date) -> "Gregorian":
        """Construct Gregorian object from a Python date object.

        :param date_object: Python date object.
        :type date_object: datetime.date
        :rtype: Gregorian
        """

        year, month, day = date_object.timetuple()[:3]
        return super().__new__(cls, year, month, day)

    def datetuple(self) -> tuple:
        """Return date as a tuple of (year, month, day)."""
        return self.year, self.month, self.day

    def dmyformat(self, separator: str = "/", padding: bool = True) -> str:
        """Return date in day-month-year format (``DD/MM/YYYY`` by default).

        :param separator: String that separates the day, month, and year values.
        :type separator: str
        :param padding: Whether to add a leading zero as a padding character to fill
            day and month values when less than 10.
        :type padding: bool
        """

        day = f"{self.day:02}" if padding else self.day
        month = f"{self.month:02}" if padding else self.month
        return f"{day}{separator}{month}{separator}{self.year}"

    def month_name(self, language: str = "en") -> str:
        """Return month name.

        :param language: Language tag for localized month name. Full locale name can
            be used, e.g. ``en-US`` or ``en_US.UTF-8``. Supported languages are
            ``en``, ``ar`` and ``bn``.
        :type language: str
        """

        return locales.get_locale(language).gregorian_month_name(self.month)

    def day_name(self, language: str = "en") -> str:
        """Return day name.

        :param language: Language tag for localized day name. Full locale name can
            be used, e.g. ``en-US`` or ``en_US.UTF-8``. Supported languages are
            ``en``, ``ar`` and ``bn``.
        :type language: str
        """

        return locales.get_locale(language).day_name(self.isoweekday())

    @staticmethod
    def notation(language: str = "en") -> str:
        """Return calendar era notation.

        :param language: Language tag for localized notation. Full locale name can
            be used, e.g. ``en-US`` or ``en_US.UTF-8``. Supported languages are
            ``en``, ``ar`` and ``bn``.
        :type language: str
        """

        return locales.get_locale(language).gregorian_notation

    def to_julian(self) -> int:
        """Return corresponding Julian day number (JDN)."""
        n = self.toordinal()
        jdn = helpers.ordinal_to_jdn(n)
        return jdn

    def to_hijri(self) -> Hijri:
        """Return Hijri object for the corresponding Gregorian date.

        :rtype: Hijri
        """
        self._check_range()
        jdn = self.to_julian()
        rjd = helpers.jdn_to_rjd(jdn)
        month_starts = ummalqura.MONTH_STARTS
        index = bisect(month_starts, rjd) - 1
        months = index + ummalqura.HIJRI_OFFSET
        years = int(months / 12)
        year = years + 1
        month = months - (years * 12) + 1
        day = rjd - month_starts[index] + 1
        return Hijri(year, month, day, validate=False)

    def _check_range(self) -> None:
        """Check if Gregorian date is within valid range."""
        min_date, max_date = ummalqura.GREGORIAN_RANGE
        if not min_date <= (self.year, self.month, self.day) <= max_date:
            raise OverflowError("date out of range")
