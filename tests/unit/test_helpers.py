from hijri_converter import helpers


def test_julian_to_ordinal():
    assert helpers.jdn_to_ordinal(2447977) == 726552


def test_ordinal_to_julian():
    assert helpers.ordinal_to_jdn(726552) == 2447977


def test_julian_to_reduced_julian():
    assert helpers.jdn_to_rjd(2456087) == 56087


def test_reduced_julian_to_julian():
    assert helpers.rjd_to_jdn(56087) == 2456087
