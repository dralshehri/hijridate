import pytest
from hijriconverter import convert


@pytest.fixture()
def hijri():
    return convert.Hijri(1410, 8, 13)


def test_ignore_validation_for_hijri_object():
    try:
        convert.Hijri(1410, 8, 30, 'lunar', validated=True)
    except TypeError or ValueError:
        pytest.fail()


def test_representation_of_hijri_object(hijri):
    assert hijri.__repr__() == 'Hijri(1410, 8, 13, lunar)'


def test_isoformat(hijri):
    assert hijri.isoformat() == '1410-08-13'


def test_year_number(hijri):
    assert hijri.year == 1410


def test_month_number(hijri):
    assert hijri.month == 8


def test_day_number(hijri):
    assert hijri.day == 13


def test_datetuple(hijri):
    assert hijri.datetuple() == (1410, 8, 13)


def test_month_days(hijri):
    assert hijri.month_days() == 29


def test_month_name(hijri):
    assert hijri.month_name() == 'Sha’ban'


def test_weekday(hijri):
    assert hijri.weekday() == 5


def test_iso_weekday(hijri):
    assert hijri.isoweekday() == 6


def test_day_name(hijri):
    assert hijri.day_name() == 'Saturday'


def test_convert_hijri_date_to_gregorian(hijri):
    assert hijri.to_gregorian().timetuple()[:3] == (1990, 3, 10)


@pytest.fixture()
def gregorian():
    return convert.Gregorian(1990, 3, 10)


def test_representation_of_gregorian_object(gregorian):
    assert repr(gregorian) == 'Gregorian(1990, 3, 10)'


def test_convert_gregorian_date_to_hijri(gregorian):
    assert gregorian.to_hijri().datetuple() == (1410, 8, 13)
