import pytest
from hijriconverter import convert, ummalqura


@pytest.fixture(scope="module")
def hijri_lunar():
    return convert.Hijri(1410, 8, 13)


@pytest.fixture(scope="module")
def hijri_solar():
    return convert.Hijri(1368, 6, 19, "solar")


@pytest.fixture(scope="module")
def gregorian():
    return convert.Gregorian(1990, 3, 10)


def test_hijri_representation(hijri_lunar):
    assert hijri_lunar.__repr__() == "Hijri(1410, 8, 13, lunar)"


def test_hijri_string_representation(hijri_lunar):
    assert hijri_lunar.__str__() == "1410-08-13"


def test_hijri_year(hijri_lunar, hijri_solar):
    assert hijri_lunar.year == 1410
    assert hijri_solar.year == 1368


def test_hijri_month(hijri_lunar):
    assert hijri_lunar.month == 8


def test_hijri_day(hijri_lunar):
    assert hijri_lunar.day == 13


def test_hijri_datetuple(hijri_lunar):
    assert hijri_lunar.datetuple() == (1410, 8, 13)


def test_hijri_isoformat(hijri_lunar):
    assert hijri_lunar.isoformat() == "1410-08-13"


def test_hijri_slashformat(hijri_lunar):
    assert hijri_lunar.slashformat() == "13/08/1410"


def test_hijri_month_days(hijri_lunar, hijri_solar):
    assert hijri_lunar.month_days() == 29
    assert hijri_solar.month_days() == 29


def test_hijri_month_name(hijri_lunar, hijri_solar):
    assert hijri_lunar.month_name() == "Sha’ban"
    assert hijri_lunar.month_name("ar") == "شعبان"
    assert hijri_solar.month_name() == "Pisces"
    assert hijri_solar.month_name("ar") == "الحوت"


def test_hijri_weekday(hijri_lunar):
    assert hijri_lunar.weekday() == 5


def test_hijri_iso_weekday(hijri_lunar):
    assert hijri_lunar.isoweekday() == 6


def test_hijri_day_name(hijri_lunar):
    assert hijri_lunar.day_name() == "Saturday"
    assert hijri_lunar.day_name("ar") == "السبت"


def test_hijri_to_julian(hijri_lunar, hijri_solar):
    assert hijri_lunar.to_julian() == 2447961
    assert hijri_solar.to_julian() == 2447961


def test_hijri_to_gregorian(hijri_lunar, hijri_solar):
    assert hijri_lunar.to_gregorian().timetuple()[:3] == (1990, 3, 10)
    assert hijri_solar.to_gregorian().timetuple()[:3] == (1990, 3, 10)


def test_gregorian_to_hijri(gregorian):
    assert gregorian.to_hijri().datetuple() == (1410, 8, 13)


def test_gregorian_valid_range(gregorian):
    try:
        gregorian._check_range()
    except ValueError:
        pytest.fail()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((1937, 3, 13), "date is out of range for conversion"),
        ((2077, 11, 17), "date is out of range for conversion"),
    ],
)
def test_gregorian_invalid_range(test_input, expected):
    with pytest.raises(ValueError) as e:
        convert.Gregorian(*test_input)._check_range()
    assert str(e.value) == expected


@pytest.mark.parametrize(
    "test_input",
    [
        (1410, 9, 30, "Lunar"),
        (1356, 1, 1, "lunar"),
        (1500, 12, 30, "lunar"),
        (1315, 6, 23, "solar"),
        (1456, 2, 25, "solar"),
    ],
)
def test_hijri_valid_date(test_input):
    year, month, day, calendar = test_input
    try:
        convert._check_hijri_date(year, month, day, calendar)
    except ValueError:
        pytest.fail()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((1410, 8, 24, "other"), "calendar must be 'lunar' or 'solar'"),
        ((37, 12, 30, "lunar"), "year must be in yyyy format"),
        ((1410, 0, 1, "lunar"), "month must be in 1..12"),
        ((1410, 13, 1, "lunar"), "month must be in 1..12"),
        ((1410, 8, 30, "lunar"), "day must be in 1..29 for month"),
        ((1368, 6, 30, "solar"), "day must be in 1..29 for month"),
        ((1355, 12, 30, "lunar"), "date is out of range for conversion"),
        ((1501, 1, 1, "lunar"), "date is out of range for conversion"),
        ((1315, 6, 22, "solar"), "date is out of range for conversion"),
        ((1456, 2, 26, "solar"), "date is out of range for conversion"),
    ],
)
def test_hijri_invalid_date(test_input, expected):
    with pytest.raises((TypeError, ValueError)) as e:
        convert._check_hijri_date(*test_input)
    assert str(e.value) == expected


def test_hijri_month_index():
    assert convert._hijri_month_index(1410, 8, ummalqura.Lunar) == 656


def test_hijri2_month_days():
    assert convert._hijri_month_days(656, ummalqura.Lunar) == 29


def test_gregorian_to_julian():
    assert convert._gregorian_to_julian(1990, 3, 26) == 2447977


def test_julian_to_gregorian():
    assert convert._julian_to_gregorian(2447977) == (1990, 3, 26)


def test_julian_to_ordinal():
    assert convert._julian_to_ordinal(2447977) == 726552


def test_ordinal_to_julian():
    assert convert._ordinal_to_julian(726552) == 2447977


def test_julian_to_reduced_julian():
    assert convert._julian_to_reduced_julian(2456087) == 56087


def test_reduced_julian_to_julian():
    assert convert._reduced_julian_to_julian(56087) == 2456087
