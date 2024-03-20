from bisect import bisect_left

import pytest

from hijridate import Hijri, helpers, ummalqura
from hijridate.ummalqura import HIJRI_RANGE

hijri_min_y, hijri_max_y = HIJRI_RANGE[0][0], HIJRI_RANGE[1][0]


def get_all_year_lengths():
    params = []
    for year in range(hijri_min_y, hijri_max_y + 1):
        date = Hijri(year, 1, 1)
        rjd = helpers.jdn_to_rjd(date.to_julian())
        month_starts = ummalqura.MONTH_STARTS
        index = bisect_left(month_starts, rjd)
        length = month_starts[index + 12] - month_starts[index]
        params += [[year, length]]
    return params


@pytest.mark.parametrize(("hijri_year", "year_length"), get_all_year_lengths())
def test_year_length(hijri_year, year_length):
    hijri_date = Hijri(hijri_year, 1, 1)
    assert hijri_date.year_length() == year_length


def get_all_month_lengths():
    params = []
    for year in range(hijri_min_y, hijri_max_y + 1):
        for month in range(1, 13):
            date = Hijri(year, month, 1)
            rjd = helpers.jdn_to_rjd(date.to_julian())
            month_starts = ummalqura.MONTH_STARTS
            index = bisect_left(month_starts, rjd)
            length = month_starts[index + 1] - month_starts[index]
            params += [[year, month, length]]
    return params


@pytest.mark.parametrize(
    ("hijri_year", "hijri_month", "month_length"), get_all_month_lengths()
)
def test_month_length(hijri_year, hijri_month, month_length):
    hijri_date = Hijri(hijri_year, hijri_month, 1)
    assert hijri_date.month_length() == month_length
