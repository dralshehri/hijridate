import pytest
from hijriconverter import helper


@pytest.mark.parametrize('test_input, expected', [
    ('Lunar', 'lunar'),
    ('SOLAR', 'solar'),
])
def test_check_hijri_calendar_with_valid_calendar(test_input, expected):
    assert expected == helper.check_hijri_calendar(test_input)


@pytest.mark.parametrize('test_input, expected', [
    (1, 'calendar must be a string'),
    ('other', 'calendar must be \'lunar\' or \'solar\''),
])
def test_check_hijri_calendar_with_invalid_calendar(test_input, expected):
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper.check_hijri_calendar(test_input)
    assert expected == str(excinfo.value)


@pytest.mark.parametrize('test_input', [
    (1410, 9, 30, 'lunar'),
    (1356, 1, 1, 'lunar'),
    (1500, 12, 30, 'lunar'),
    (1315, 6, 23, 'solar'),
    (1456, 2, 25, 'solar'),
    (2016, 2, 29, 'gregorian'),
    (1990, 10, 31, 'gregorian'),
    (1937, 3, 14, 'gregorian'),
    (2077, 11, 16, 'gregorian'),
])
def test_check_date_with_valid_date(test_input):
    year, month, day, calendar = test_input
    assert (year, month, day) == helper.check_date(year, month, day, calendar)


@pytest.mark.parametrize('test_input, expected', [
    (('y', 8, 'n', 'lunar'), 'year must be an integer'),
    ((17, 2, 28, 'gregorian'), 'year must be in yyyy format'),
    ((2017, 'm', 28, 'gregorian'), 'month must be an integer'),
    ((2017, 0, 28, 'gregorian'), 'month must be in 1..12'),
    ((2017, 13, 28, 'gregorian'), 'month must be in 1..12'),
    ((1410, 8, 'd', 'lunar'), 'day must be an integer'),
    ((1410, 8, 30, 'lunar'), 'day must be in 1..29 for month'),
    ((1368, 6, 30, 'solar'), 'day must be in 1..29 for month'),
    ((2017, 2, 29, 'gregorian'), 'day must be in 1..28 for month'),
    ((1990, 11, 31, 'gregorian'), 'day must be in 1..30 for month'),
    ((1355, 12, 30, 'lunar'), 'date is out of range for conversion'),
    ((1501, 1, 1, 'lunar'), 'date is out of range for conversion'),
    ((1315, 6, 22, 'solar'), 'date is out of range for conversion'),
    ((1456, 2, 26, 'solar'), 'date is out of range for conversion'),
    ((1456, 2, 26, 'gregorian'), 'date is out of range for conversion'),
    ((1456, 2, 26, 'gregorian'), 'date is out of range for conversion'),
])
def test_check_date_with_invalid_date(test_input, expected):
    year, month, day, calendar = test_input
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper.check_date(year, month, day, calendar)
    assert expected == str(excinfo.value)


def test_hijri_month_index():
    assert helper.hijri_month_index(1410, 8, 'lunar') == 656


def test_hijri_month_days():
    assert helper.hijri_month_days(1410, 8, 'lunar') == 29


def test_convert_hijri_date_to_julian_day():
    assert helper.hijri_to_julian(1410, 8, 13, 'lunar') == 2447961


def test_convert_gregorian_date_to_julian_day():
    assert helper.gregorian_to_julian(1990, 3, 26) == 2447977


def test_convert_julian_day_to_gregorian_date():
    assert helper.julian_to_gregorian(2447977) == (1990, 3, 26)


def test_convert_julian_day_to_modified_julian_day():
    assert helper.julian_to_modified_julian(2456087) == 56087


def test_convert_modified_julian_day_to_julian_day():
    assert helper.modified_julian_to_julian(56087) == 2456087
