import pytest
from hijriconverter import convert


@pytest.fixture()
def hijri():
    return convert.Hijri(1410, 8, 13)


def test_representation_of_hijri(hijri):
    assert hijri.__repr__() == "Hijri(1410, 8, 13, lunar)"


def test_string_representation_of_hijri(hijri):
    assert hijri.__str__() == "1410-08-13"


def test_isoformat(hijri):
    assert hijri.isoformat() == "1410-08-13"


def test_year(hijri):
    assert hijri.year == 1410


def test_month(hijri):
    assert hijri.month == 8


def test_day(hijri):
    assert hijri.day == 13


def test_datetuple(hijri):
    assert hijri.datetuple() == (1410, 8, 13)


def test_slashformat(hijri):
    assert hijri.slashformat() == "13/08/1410"


def test_month_days(hijri):
    assert hijri.month_days() == 29


def test_month_name(hijri):
    assert hijri.month_name() == "Sha’ban"


def test_weekday(hijri):
    assert hijri.weekday() == 5


def test_iso_weekday(hijri):
    assert hijri.isoweekday() == 6


def test_day_name(hijri):
    assert hijri.day_name() == "Saturday"


def test_convert_hijri_to_gregorian(hijri):
    assert hijri.to_gregorian().timetuple()[:3] == (1990, 3, 10)


@pytest.fixture()
def gregorian():
    return convert.Gregorian(1990, 3, 10)


def test_representation_of_gregorian_object(gregorian):
    assert repr(gregorian) == "Gregorian(1990, 3, 10)"


def test_convert_gregorian_to_hijri(gregorian):
    assert gregorian.to_hijri().datetuple() == (1410, 8, 13)


def test_raise_exception_with_invalid_hijri_date(hijri):
    with pytest.raises((TypeError, ValueError)):
        convert.Hijri(1310, 8, 13, validate=True)


def test_raise_exception_with_invalid_gregorian_date(hijri):
    with pytest.raises((TypeError, ValueError)):
        convert.Gregorian(1890, 3, 10, validate=True)


@pytest.mark.parametrize(
    "test_input",
    [
        (1410, 9, 30, "lunar"),
        (1356, 1, 1, "lunar"),
        (1500, 12, 30, "lunar"),
        (1315, 6, 23, "solar"),
        (1456, 2, 25, "solar"),
        (2016, 2, 29, "gregorian"),
        (1990, 10, 31, "gregorian"),
        (1937, 3, 14, "gregorian"),
        (2077, 11, 16, "gregorian"),
    ],
)
def test_check_valid_date(test_input):
    year, month, day, calendar = test_input
    expected = convert._check_date(year, month, day, calendar)
    assert (year, month, day, calendar) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((1410, 8, 24, 0), "calendar must be a string"),
        ((1410, 8, 24, "other"), "calendar must be 'lunar' or 'solar'"),
        (("y", 8, "n", "lunar"), "year must be an integer"),
        ((17, 2, 28, "gregorian"), "year must be in yyyy format"),
        ((2017, "m", 28, "gregorian"), "month must be an integer"),
        ((2017, 0, 28, "gregorian"), "month must be in 1..12"),
        ((2017, 13, 28, "gregorian"), "month must be in 1..12"),
        ((1410, 8, "d", "lunar"), "day must be an integer"),
        ((1410, 8, 30, "lunar"), "day must be in 1..29 for month"),
        ((1368, 6, 30, "solar"), "day must be in 1..29 for month"),
        ((2017, 2, 29, "gregorian"), "day must be in 1..28 for month"),
        ((1990, 11, 31, "gregorian"), "day must be in 1..30 for month"),
        ((1355, 12, 30, "lunar"), "date is out of range for conversion"),
        ((1501, 1, 1, "lunar"), "date is out of range for conversion"),
        ((1315, 6, 22, "solar"), "date is out of range for conversion"),
        ((1456, 2, 26, "solar"), "date is out of range for conversion"),
        ((1456, 2, 26, "gregorian"), "date is out of range for conversion"),
        ((1456, 2, 26, "gregorian"), "date is out of range for conversion"),
    ],
)
def test_check_invalid_date(test_input, expected):
    year, month, day, calendar = test_input
    with pytest.raises((TypeError, ValueError)) as excinfo:
        convert._check_date(year, month, day, calendar)
    assert expected == str(excinfo.value)


def test_hijri_month_index():
    assert convert._hijri_month_index(1410, 8, "lunar") == 656


def test_hijri_month_days():
    assert convert._hijri_month_days(1410, 8, "lunar") == 29


def test_convert_hijri_to_julian():
    assert convert._hijri_to_julian(1410, 8, 13, "lunar") == 2447961


def test_convert_gregorian_to_julian():
    assert convert._gregorian_to_julian(1990, 3, 26) == 2447977


def test_convert_julian_to_gregorian():
    assert convert._julian_to_gregorian(2447977) == (1990, 3, 26)


def test_convert_julian_to_modified_julian():
    assert convert._julian_to_modified_julian(2456087) == 56087


def test_convert_modified_julian_to_julian():
    assert convert._modified_julian_to_julian(56087) == 2456087
