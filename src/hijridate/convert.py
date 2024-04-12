"""Main module of the HijriDate package."""

import datetime

from bisect import bisect
from typing import Tuple

from hijridate import helpers, locales, ummalqura


class Hijri:
    """A Hijri object represents a date in lunar Hijri calendar.

    Args:
        year: Hijri year.
        month: Hijri month.
        day: Hijri day.
        validate: Whether to validate Hijri input or not. It's recommended
            to keep the default for accurate conversion.

    Raises:
        OverflowError: When ``year`` is out of supported Hijri range.
        ValueError: When ``month`` is not within the range of `1-12`.
        ValueError: When ``day`` is not within the range of
            `1-month_length` for month.
    """

    __slots__ = "_year", "_month", "_day"

    def __init__(self, year: int, month: int, day: int, *, validate: bool = True):
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
        self_date = self.datetuple()
        other_date = other.datetuple()
        return 0 if self_date == other_date else 1 if self_date > other_date else -1

    @classmethod
    def fromisoformat(cls, date_string: str) -> "Hijri":
        """Construct Hijri object from an ISO formatted Hijri date.

        Args:
            date_string: Hijri date in ISO format ``YYYY-MM-DD``.
        """
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    @classmethod
    def today(cls) -> "Hijri":
        """Construct Hijri object from today's date."""
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

    def datetuple(self) -> Tuple[int, int, int]:
        """Return date as a tuple of (year, month, day)."""
        return self._year, self._month, self._day

    def isoformat(self) -> str:
        """Return date in ISO format i.e. ``YYYY-MM-DD``."""
        return f"{self._year:04}-{self._month:02}-{self._day:02}"

    def dmyformat(self, separator: str = "/", *, padding: bool = True) -> str:
        """Return date in day-month-year format (``DD/MM/YYYY`` by default).

        Args:
            separator: String that separates the day, month, and year values.
            padding: Whether to add a leading zero as a padding character to
                fill day and month values when less than 10.
        """
        day = f"{self._day:02}" if padding else self._day
        month = f"{self._month:02}" if padding else self._month
        return f"{day}{separator}{month}{separator}{self._year}"

    def year_length(self) -> int:
        """Return number of days in year."""
        month_starts = ummalqura.MONTH_STARTS
        first_index, last_index = self._year_indexes()
        return month_starts[last_index + 1] - month_starts[first_index]

    def month_length(self) -> int:
        """Return number of days in month."""
        month_starts = ummalqura.MONTH_STARTS
        index = self._month_index()
        return month_starts[index + 1] - month_starts[index]

    def month_name(self, language: locales.Language = "en") -> str:
        """Return month name.

        Args:
            language: Two-letter language code for localized month name.
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

    def day_name(self, language: locales.Language = "en") -> str:
        """Return day name.

        Args:
            language: Two-letter language code for localized day name.
        """
        return locales.get_locale(language).day_name(self.isoweekday())

    @staticmethod
    def notation(language: locales.Language = "en") -> str:
        """Return calendar era notation.

        Args:
            language: Two-letter language code for localized era notation.
        """
        return locales.get_locale(language).notation

    def to_julian(self) -> int:
        """Return corresponding Julian day number (JDN)."""
        month_starts = ummalqura.MONTH_STARTS
        index = self._month_index()
        rjd = month_starts[index] + self._day - 1
        return helpers.rjd_to_jdn(rjd)

    def to_gregorian(self) -> "Gregorian":
        """Return Gregorian object for the corresponding Hijri date."""
        jdn = self.to_julian()
        ordinal = helpers.jdn_to_ordinal(jdn)
        return Gregorian.fromordinal(ordinal)

    def _check_date(self) -> None:
        """Check date values if within valid range."""
        # check year
        min_year, max_year = (d[0] for d in ummalqura.HIJRI_RANGE)
        if not min_year <= self.year <= max_year:
            message = f"year must be in {min_year}-{max_year}, got '{self.year}'"
            raise OverflowError(message)
        # check month
        max_months = 12
        if not 1 <= self.month <= max_months:
            message = f"month must be in 1-{max_months}, got '{self.month}'"
            raise ValueError(message)
        # check day
        month_length = self.month_length()
        if not 1 <= self.day <= month_length:
            message = f"day must be in 1-{month_length} for month, got '{self.day}'"
            raise ValueError(message)

    def _year_indexes(self) -> Tuple[int, int]:
        """Return year's first and last indexes in ummalqura month starts."""
        prior_months = (self.year - 1) * 12
        first_index = prior_months - ummalqura.HIJRI_OFFSET
        last_index = first_index + 11
        return first_index, last_index

    def _month_index(self) -> int:
        """Return month's index in ummalqura month starts."""
        prior_months = ((self.year - 1) * 12) + self.month - 1
        return prior_months - ummalqura.HIJRI_OFFSET


class Gregorian(datetime.date):
    """A Gregorian object represents a date in Gregorian calendar.

    Args:
        year (int): Gregorian year.
        month (int): Gregorian month.
        day (int): Gregorian day.
    """

    __slots__ = ()

    @classmethod
    def fromdate(cls, date_object: datetime.date) -> "Gregorian":
        """Construct Gregorian object from a Python date object.

        Args:
            date_object: Python date object.
        """
        year, month, day = date_object.timetuple()[:3]
        return cls(year, month, day)

    def datetuple(self) -> Tuple[int, int, int]:
        """Return date as a tuple of (year, month, day)."""
        return self.year, self.month, self.day

    def dmyformat(self, separator: str = "/", *, padding: bool = True) -> str:
        """Return date in day-month-year format (``DD/MM/YYYY`` by default).

        Args:
            separator: String that separates the day, month, and year values.
            padding: Whether to add a leading zero as a padding character to
                fill day and month values when less than 10.
        """
        day = f"{self.day:02}" if padding else self.day
        month = f"{self.month:02}" if padding else self.month
        return f"{day}{separator}{month}{separator}{self.year}"

    def month_name(self, language: locales.Language = "en") -> str:
        """Return month name.

        Args:
            language: Two-letter language code for localized month name.
        """
        return locales.get_locale(language).gregorian_month_name(self.month)

    def day_name(self, language: locales.Language = "en") -> str:
        """Return day name.

        Args:
            language: Two-letter language code for localized day name.
        """
        return locales.get_locale(language).day_name(self.isoweekday())

    @staticmethod
    def notation(language: locales.Language = "en") -> str:
        """Return calendar era notation.

        Args:
            language: Two-letter language code for localized era notation.
        """
        return locales.get_locale(language).gregorian_notation

    def to_julian(self) -> int:
        """Return corresponding Julian day number (JDN)."""
        ordinal = self.toordinal()
        return helpers.ordinal_to_jdn(ordinal)

    def to_hijri(self) -> Hijri:
        """Return Hijri object for the corresponding Gregorian date.

        Raises:
            OverflowError: When date is out of supported Gregorian range.
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
            min_date_iso = "-".join([f"{i:02}" for i in min_date])
            max_date_iso = "-".join([f"{i:02}" for i in max_date])
            message = (
                f"date must be in '{min_date_iso}'-'{max_date_iso}', "
                f"got '{self.isoformat()}'"
            )
            raise OverflowError(message)
