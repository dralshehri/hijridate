from datetime import date

import pytest

from hijridate.convert import Gregorian, Hijri
from hijridate.ummalqura import GREGORIAN_RANGE, HIJRI_RANGE

h_min, h_max = HIJRI_RANGE
g_min, g_max = GREGORIAN_RANGE
g_min_iso = "-".join([f"{i:02}" for i in g_min])
g_max_iso = "-".join([f"{i:02}" for i in g_max])


def test_importing_at_init_module():
    from hijridate import Gregorian, Hijri

    assert Hijri(1410, 8, 13)
    assert Gregorian(1990, 3, 10)


@pytest.fixture(scope="class")
def _hijri_date(request):
    request.cls.hijri_date = Hijri(1410, 8, 13)


@pytest.mark.usefixtures("_hijri_date")
class TestHijri:
    hijri_date = None

    def test_representation(self):
        assert self.hijri_date.__repr__() == "Hijri(1410, 8, 13)"

    def test_string_representation(self):
        assert self.hijri_date.__str__() == "1410-08-13"

    def test_hash(self):
        assert self.hijri_date.__hash__() == hash(("Hijri", 1410, 8, 13))

    @pytest.mark.parametrize("attr", ["__gt__", "__ge__", "__lt__", "__le__"])
    def test_comparison_notimplemented(self, attr):
        assert getattr(self.hijri_date, attr)("1410-08-13") == NotImplemented

    def test_equality(self):
        assert self.hijri_date == Hijri(1410, 8, 13)
        assert self.hijri_date != Hijri(1410, 8, 14)
        assert self.hijri_date != "1410-08-13"

    def test_ordering(self):
        assert self.hijri_date > Hijri(1410, 8, 12)
        assert self.hijri_date >= Hijri(1410, 8, 13)
        assert self.hijri_date < Hijri(1410, 8, 14)
        assert self.hijri_date <= Hijri(1410, 8, 13)

    def test_fromisoformat(self):
        assert Hijri.fromisoformat("1410-08-13") == self.hijri_date

    def test_today(self):
        assert Hijri.today().to_gregorian() == Gregorian.today()

    def test_year(self):
        assert self.hijri_date.year == 1410

    def test_month(self):
        assert self.hijri_date.month == 8

    def test_day(self):
        assert self.hijri_date.day == 13

    def test_datetuple(self):
        assert self.hijri_date.datetuple() == (1410, 8, 13)

    def test_isoformat(self):
        assert self.hijri_date.isoformat() == "1410-08-13"

    def test_dmyformat(self):
        assert self.hijri_date.dmyformat() == "13/08/1410"
        assert self.hijri_date.dmyformat(padding=False) == "13/8/1410"
        assert self.hijri_date.dmyformat(separator=".") == "13.08.1410"

    def test_year_length(self):
        assert self.hijri_date.year_length() == 355

    def test_month_length(self):
        assert self.hijri_date.month_length() == 29

    def test_month_name(self):
        assert self.hijri_date.month_name() == "Sha'ban"
        assert self.hijri_date.month_name("en") == "Sha'ban"
        assert self.hijri_date.month_name("en-US") == "Sha'ban"
        assert self.hijri_date.month_name("tr") == "Şaban"

    def test_weekday(self):
        assert self.hijri_date.weekday() == 5

    def test_iso_weekday(self):
        assert self.hijri_date.isoweekday() == 6

    def test_day_name(self):
        assert self.hijri_date.day_name() == "Saturday"
        assert self.hijri_date.day_name("en") == "Saturday"
        assert self.hijri_date.day_name("en-US") == "Saturday"
        assert self.hijri_date.day_name("tr") == "Cumartesi"

    def test_notation(self):
        assert self.hijri_date.notation() == "AH"
        assert self.hijri_date.notation("en") == "AH"
        assert self.hijri_date.notation("en-US") == "AH"
        assert self.hijri_date.notation("tr") == "Hicri"

    def test_to_julian(self):
        assert self.hijri_date.to_julian() == 2447961

    def test_to_gregorian(self):
        assert self.hijri_date.to_gregorian().datetuple() == (1990, 3, 10)

    def test_month_index(self):
        assert self.hijri_date._month_index() == 811

    @pytest.mark.parametrize(
        "datetuple",
        [(1410, 9, 30), (1356, 1, 1), (1500, 12, 30)],
    )
    def test_valid_date(self, datetuple):
        year, month, day = datetuple
        Hijri(year, month, day, validate=True)

    @pytest.mark.parametrize(
        ("datetuple", "err_message"),
        [
            (
                (37, 12, 30),
                f"year must be in {h_min[0]}-{h_max[0]}, got '37'",
            ),
            (
                (1342, 12, 29),
                f"year must be in {h_min[0]}-{h_max[0]}, got '1342'",
            ),
            (
                (1501, 1, 1),
                f"year must be in {h_min[0]}-{h_max[0]}, got '1501'",
            ),
        ],
    )
    def test_invalid_year(self, datetuple, err_message):
        with pytest.raises(OverflowError, match=err_message):
            Hijri(*datetuple, validate=True)

    @pytest.mark.parametrize(
        ("datetuple", "err_message"),
        [
            ((1410, 0, 1), "month must be in 1-12, got '0'"),
            ((1410, 13, 1), "month must be in 1-12, got '13'"),
            ((1410, 8, 30), "day must be in 1-29 for month, got '30'"),
        ],
    )
    def test_invalid_day_or_month(self, datetuple, err_message):
        with pytest.raises(ValueError, match=err_message):
            Hijri(*datetuple, validate=True)


@pytest.fixture(scope="class")
def _gregorian_date(request):
    request.cls.gregorian_date = Gregorian(1990, 3, 10)


@pytest.mark.usefixtures("_gregorian_date")
class TestGregorian:
    gregorian_date = None

    def test_fromdate(self):
        test_date = date(2014, 12, 28)
        assert Gregorian.fromdate(test_date).datetuple() == (2014, 12, 28)

    def test_datetuple(self):
        assert self.gregorian_date.datetuple() == (1990, 3, 10)

    def test_dmyformat(self):
        assert self.gregorian_date.dmyformat() == "10/03/1990"
        assert self.gregorian_date.dmyformat(padding=False) == "10/3/1990"
        assert self.gregorian_date.dmyformat(separator=".") == "10.03.1990"

    def test_month_name(self):
        assert self.gregorian_date.month_name() == "March"
        assert self.gregorian_date.month_name("en") == "March"
        assert self.gregorian_date.month_name("en-US") == "March"
        assert self.gregorian_date.month_name("tr") == "Mart"

    def test_day_name(self):
        assert self.gregorian_date.day_name() == "Saturday"
        assert self.gregorian_date.day_name("en") == "Saturday"
        assert self.gregorian_date.day_name("en-US") == "Saturday"
        assert self.gregorian_date.day_name("tr") == "Cumartesi"

    def test_notation(self):
        assert self.gregorian_date.notation() == "CE"
        assert self.gregorian_date.notation("en") == "CE"
        assert self.gregorian_date.notation("en-US") == "CE"
        assert self.gregorian_date.notation("tr") == "Miladi"

    def test_to_julian(self):
        assert self.gregorian_date.to_julian() == 2447961

    def test_to_hijri(self):
        assert self.gregorian_date.to_hijri().datetuple() == (1410, 8, 13)

    @pytest.mark.parametrize(
        "datetuple",
        [(1990, 3, 10), (1924, 8, 1), (2077, 11, 16)],
    )
    def test_valid_range(self, datetuple):
        year, month, day = datetuple
        Gregorian(year, month, day)._check_range()

    @pytest.mark.parametrize(
        ("datetuple", "err_message"),
        [
            (
                (1924, 7, 31),
                f"date must be in '{g_min_iso}'-'{g_max_iso}', got '1924-07-31'",
            ),
            (
                (2077, 11, 17),
                f"date must be in '{g_min_iso}'-'{g_max_iso}', got '2077-11-17'",
            ),
        ],
    )
    def test_invalid_range(self, datetuple, err_message):
        with pytest.raises(OverflowError, match=err_message):
            Gregorian(*datetuple)._check_range()
