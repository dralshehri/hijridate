import pytest
from hijriconverter import helper


@pytest.mark.parametrize('test_input', [
    (1410, 9, 30, 'lunar'),
    (1356, 1, 1, 'lunar'),
    (1500, 12, 30, 'lunar'),
    (1315, 6, 23, 'solar'),
    (1456, 2, 25, 'solar'),
])
def test_valid_hijri_date(test_input):
    year, month, day, calendar = test_input
    assert helper.validate_hijri_date(year, month, day, calendar)


@pytest.mark.parametrize('test_input', [
    (2016, 2, 29),
    (1990, 10, 31),
    (1937, 3, 14),
    (2077, 11, 16),
])
def test_valid_gregorian_date(test_input):
    year, month, day = test_input
    assert helper.validate_gregorian_date(year, month, day)


@pytest.mark.parametrize('test_input, expected', [
    (1, 'calendar must be a string'),
    ('other', 'calendar must be lunar or solar'),
])
def test_check_hijri_calendar_with_invalid_calendar(test_input, expected):
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper._check_hijri_calendar(test_input)
    assert expected == str(excinfo.value)


@pytest.mark.parametrize('test_input, expected', [
    ('n', 'year must be an integer'),
    (10, 'year must be in YYYY format'),
])
def test_check_year_with_invalid_year(test_input, expected):
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper._check_year(test_input)
    assert expected == str(excinfo.value)


@pytest.mark.parametrize('test_input, expected', [
    ('n', 'month must be an integer'),
    (18, 'month must be in 1..12'),
])
def test_check_month_with_invalid_month(test_input, expected):
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper._check_month(test_input)
    assert expected == str(excinfo.value)


@pytest.mark.parametrize('test_input, expected', [
    ((1410, 8, 'n', 'lunar'), 'day must be an integer'),
    ((1410, 8, 30, 'lunar'), 'day is out of range for month'),
    ((1368, 6, 30, 'solar'), 'day is out of range for month'),
    ((2017, 2, 29, 'gregorian'), 'day is out of range for month'),
    ((1990, 11, 31, 'gregorian'), 'day is out of range for month'),
])
def test_check_day_with_invalid_day(test_input, expected):
    year, month, day, calendar = test_input
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper._check_day(year, month, day, calendar)
    assert expected == str(excinfo.value)


@pytest.mark.parametrize('test_input', [
    (1355, 12, 30, 'lunar'),
    (1501, 1, 1, 'lunar'),
    (1315, 6, 22, 'solar'),
    (1456, 2, 26, 'solar'),
    (1456, 2, 26, 'gregorian'),
    (1456, 2, 26, 'gregorian'),
])
def test_check_date_range_with_date_out_of_range(test_input):
    year, month, day, calendar = test_input
    with pytest.raises((TypeError, ValueError)) as excinfo:
        helper._check_date_range(year, month, day, calendar)
    assert str(excinfo.value) == 'date is out of range for conversion'


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
