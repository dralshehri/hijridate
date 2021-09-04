"""Helper methods for Hijri conversion."""


def jdn_to_ordinal(jdn: int) -> int:
    """Convert Julian day number (JDN) to date ordinal number.

    :param jdn: Julian day number (JDN).
    :type jdn: int
    """

    return jdn - 1721425


def ordinal_to_jdn(n: int) -> int:
    """Convert date ordinal number to Julian day number (JDN).

    :param n: Date ordinal number.
    :type n: int
    """

    return n + 1721425


def jdn_to_rjd(jdn: int) -> int:
    """Return Reduced Julian Day (RJD) number from Julian day number (JDN).

    :param jdn: Julian day number (JDN).
    :type jdn: int
    """

    return jdn - 2400000


def rjd_to_jdn(rjd: int) -> int:
    """Return Julian day number (JDN) from Reduced Julian Day (RJD) number.

    :param rjd: Reduced Julian Day (RJD) number.
    :type rjd: int
    """

    return rjd + 2400000
