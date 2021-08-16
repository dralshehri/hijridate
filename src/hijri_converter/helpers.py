"""Helper methods for Hijri conversion."""


def julian_to_ordinal(jd: int) -> int:
    """Convert Julian Day (JD) number to ordinal number."""
    return jd - 1721425


def ordinal_to_julian(n: int) -> int:
    """Convert ordinal number to Julian Day (JD) number."""
    return n + 1721425


def julian_to_reduced_julian(jd: int) -> int:
    """Convert Julian Day (JD) number to Reduced Julian Day (RJD) number."""
    return jd - 2400000


def reduced_julian_to_julian(rjd: int) -> int:
    """Convert Reduced Julian Day (RJD) number to Julian Day (JD) number."""
    return rjd + 2400000
