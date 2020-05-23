import pytest
from datetime import date
from hijri_converter import convert


@pytest.fixture(scope="module")
def hijri():
    return convert.Hijri(1410, 8, 13)


@pytest.fixture(scope="module")
def gregorian():
    return convert.Gregorian(1990, 3, 10)


def test_hijri_representation(hijri):
    assert hijri.__repr__() == "Hijri(1410, 8, 13)"


def test_hijri_string_representation(hijri):
    assert hijri.__str__() == "1410-08-13"


def test_hijri_hash(hijri):
    assert hijri.__hash__() == hash(("Hijri", 1410, 8, 13))


@pytest.mark.parametrize(
    "test_input", ["__gt__", "__ge__", "__lt__", "__le__"]
)
def test_test_hijri_comparison_exception(hijri, test_input):
    with pytest.raises(TypeError) as e:
        getattr(hijri, test_input)("1410-08-13")
    assert str(e.value) == "can't compare 'Hijri' to 'str'"


def test_hijri_equality(hijri):
    assert hijri == convert.Hijri(1410, 8, 13)
    assert hijri != convert.Hijri(1410, 8, 14)
    assert hijri != "1410-08-13"


def test_hijri_ordering(hijri):
    assert hijri > convert.Hijri(1410, 8, 12)
    assert hijri >= convert.Hijri(1410, 8, 13)
    assert hijri < convert.Hijri(1410, 8, 14)
    assert hijri <= convert.Hijri(1410, 8, 13)


def test_hijri_fromisoformat(hijri):
    assert convert.Hijri.fromisoformat("1410-08-13") == hijri


def test_hijri_year(hijri):
    assert hijri.year == 1410


def test_hijri_month(hijri):
    assert hijri.month == 8


def test_hijri_day(hijri):
    assert hijri.day == 13


def test_hijri_datetuple(hijri):
    assert hijri.datetuple() == (1410, 8, 13)


def test_hijri_isoformat(hijri):
    assert hijri.isoformat() == "1410-08-13"


def test_hijri_dmyformat(hijri):
    assert hijri.dmyformat() == "13/08/1410"


def test_hijri_slashformat_deprecation(hijri):
    with pytest.deprecated_call():
        hijri.slashformat()


def test_hijri_month_length(hijri):
    assert hijri.month_length() == 29


def test_hijri_month_name(hijri):
    assert hijri.month_name() == "Sha’ban"
    assert hijri.month_name("ar") == "شعبان"


def test_hijri_weekday(hijri):
    assert hijri.weekday() == 5


def test_hijri_iso_weekday(hijri):
    assert hijri.isoweekday() == 6


def test_hijri_day_name(hijri):
    assert hijri.day_name() == "Saturday"
    assert hijri.day_name("ar") == "السبت"


def test_hijri_notation(hijri):
    assert hijri.notation() == "AH"
    assert hijri.notation("ar") == "هـ"


def test_hijri_to_julian(hijri):
    assert hijri.to_julian() == 2447961


def test_hijri_to_gregorian(hijri):
    assert hijri.to_gregorian().datetuple() == (1990, 3, 10)


def test_hijri_month_index(hijri):
    assert hijri._month_index() == 811


@pytest.mark.parametrize(
    "test_input", [(1410, 9, 30), (1356, 1, 1), (1500, 12, 30)]
)
def test_hijri_valid_date(test_input):
    year, month, day = test_input
    try:
        convert.Hijri(year, month, day, validate=False)._check_date()
    except (ValueError, OverflowError):
        pytest.fail()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((37, 12, 30), "date out of range"),
        ((1342, 12, 29), "date out of range"),
        ((1501, 1, 1), "date out of range"),
        ((1410, 0, 1), "month must be in 1..12"),
        ((1410, 13, 1), "month must be in 1..12"),
        ((1410, 8, 30), "day must be in 1..29 for month"),
    ],
)
def test_hijri_invalid_date(test_input, expected):
    with pytest.raises((ValueError, OverflowError)) as e:
        convert.Hijri(*test_input, validate=False)._check_date()
    assert str(e.value) == expected


def test_gregorian_fromdate():
    test_date = date(2014, 12, 28)
    assert convert.Gregorian.fromdate(test_date).datetuple() == (2014, 12, 28)


def test_gregorian_datetuple(gregorian):
    assert gregorian.datetuple() == (1990, 3, 10)


def test_gregorian_dmyformat(gregorian):
    assert gregorian.dmyformat() == "10/03/1990"


def test_gregorian_slashformat_deprecation(gregorian):
    with pytest.deprecated_call():
        gregorian.slashformat()


def test_gregorian_month_name(gregorian):
    assert gregorian.month_name() == "March"
    assert gregorian.month_name("ar") == "مارس"


def test_gregorian_day_name(gregorian):
    assert gregorian.day_name() == "Saturday"
    assert gregorian.day_name("ar") == "السبت"


def test_gregorian_notation(gregorian):
    assert gregorian.notation() == "CE"
    assert gregorian.notation("ar") == "م"


def test_gregorian_to_julian(gregorian):
    assert gregorian.to_julian() == 2447961


def test_gregorian_to_hijri(gregorian):
    assert gregorian.to_hijri().datetuple() == (1410, 8, 13)


@pytest.mark.parametrize(
    "test_input", [(1990, 3, 10), (1924, 8, 1), (2077, 11, 16)]
)
def test_gregorian_valid_range(test_input):
    year, month, day = test_input
    try:
        convert.Gregorian(year, month, day)._check_range()
    except OverflowError:
        pytest.fail()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((1924, 7, 31), "date out of range"),
        ((2077, 11, 17), "date out of range"),
    ],
)
def test_gregorian_invalid_range(test_input, expected):
    with pytest.raises(OverflowError) as e:
        convert.Gregorian(*test_input)._check_range()
    assert str(e.value) == expected


def test_julian_to_ordinal():
    assert convert._julian_to_ordinal(2447977) == 726552


def test_ordinal_to_julian():
    assert convert._ordinal_to_julian(726552) == 2447977


def test_julian_to_reduced_julian():
    assert convert._julian_to_reduced_julian(2456087) == 56087


def test_reduced_julian_to_julian():
    assert convert._reduced_julian_to_julian(56087) == 2456087
