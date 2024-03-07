import pytest

from hijridate import Hijri, ummalqura
from hijridate.ummalqura import HIJRI_RANGE

hijri_min_y, hijri_max_y = HIJRI_RANGE[0][0], HIJRI_RANGE[1][0]


def generate_year_deltas():
    params = []
    for year in range(hijri_min_y, hijri_max_y + 1):
        first_date = Hijri(year, 1, 1)
        last_month_length = Hijri(year, 12, 1).month_length()
        last_date = Hijri(year, 12, last_month_length)
        delta = (last_date.to_gregorian() - first_date.to_gregorian()).days + 1
        params += [[year, delta]]
    return params


@pytest.mark.parametrize("test_input, expected", generate_year_deltas())
def test_year_length(test_input, expected):
    print(test_input, expected)
    hijri_date = Hijri(test_input, 1, 1)
    assert hijri_date.year_length() == expected


def generate_month_deltas():
    params = []
    for year in range(hijri_min_y, hijri_max_y + 1):
        for month in range(1, 13):
            first_date = Hijri(year, month, 1)
            month_length = Hijri(year, month, 1).month_length()
            last_date = Hijri(year, month, month_length)
            delta = (
                last_date.to_gregorian() - first_date.to_gregorian()
            ).days + 1
            params += [[(year, month), delta]]
    return params


@pytest.mark.parametrize("test_input, expected", generate_month_deltas())
def test_month_length(test_input, expected):
    hijri_date = Hijri(test_input[0], test_input[1], 1)
    assert hijri_date.month_length() == expected
