from datetime import date

import pytest

from hijri_converter import convert


def test_importing_at_init_module():
    from hijri_converter import Gregorian, Hijri

    assert Hijri(1410, 8, 13)
    assert Gregorian(1990, 3, 10)


@pytest.fixture(scope="class")
def hijri_obj(request):
    request.cls.hijri_obj = convert.Hijri(1410, 8, 13)


@pytest.mark.usefixtures("hijri_obj")
class TestHijri:
    def test_representation(self):
        assert self.hijri_obj.__repr__() == "Hijri(1410, 8, 13)"

    def test_string_representation(self):
        assert self.hijri_obj.__str__() == "1410-08-13"

    def test_hash(self):
        assert self.hijri_obj.__hash__() == hash(("Hijri", 1410, 8, 13))

    @pytest.mark.parametrize("test_input", ["__gt__", "__ge__", "__lt__", "__le__"])
    def test_comparison_notimplemented(self, test_input):
        assert getattr(self.hijri_obj, test_input)("1410-08-13") == NotImplemented

    def test_equality(self):
        assert self.hijri_obj == convert.Hijri(1410, 8, 13)
        assert self.hijri_obj != convert.Hijri(1410, 8, 14)
        assert self.hijri_obj != "1410-08-13"

    def test_ordering(self):
        assert self.hijri_obj > convert.Hijri(1410, 8, 12)
        assert self.hijri_obj >= convert.Hijri(1410, 8, 13)
        assert self.hijri_obj < convert.Hijri(1410, 8, 14)
        assert self.hijri_obj <= convert.Hijri(1410, 8, 13)

    def test_fromisoformat(self):
        assert convert.Hijri.fromisoformat("1410-08-13") == self.hijri_obj

    def test_today(self):
        assert convert.Hijri.today().to_gregorian() == convert.Gregorian.today()

    def test_year(self):
        assert self.hijri_obj.year == 1410

    def test_month(self):
        assert self.hijri_obj.month == 8

    def test_day(self):
        assert self.hijri_obj.day == 13

    def test_datetuple(self):
        assert self.hijri_obj.datetuple() == (1410, 8, 13)

    def test_isoformat(self):
        assert self.hijri_obj.isoformat() == "1410-08-13"

    def test_dmyformat(self):
        assert self.hijri_obj.dmyformat() == "13/08/1410"
        assert self.hijri_obj.dmyformat(padding=False) == "13/8/1410"
        assert self.hijri_obj.dmyformat(separator=".") == "13.08.1410"

    def test_month_length(self):
        assert self.hijri_obj.month_length() == 29

    def test_month_name(self):
        assert self.hijri_obj.month_name() == "Sha’ban"
        assert self.hijri_obj.month_name("en") == "Sha’ban"
        assert self.hijri_obj.month_name("en-US") == "Sha’ban"

    def test_weekday(self):
        assert self.hijri_obj.weekday() == 5

    def test_iso_weekday(self):
        assert self.hijri_obj.isoweekday() == 6

    def test_day_name(self):
        assert self.hijri_obj.day_name() == "Saturday"
        assert self.hijri_obj.day_name("en") == "Saturday"
        assert self.hijri_obj.day_name("en-US") == "Saturday"

    def test_notation(self):
        assert self.hijri_obj.notation() == "AH"
        assert self.hijri_obj.notation("en") == "AH"
        assert self.hijri_obj.notation("en-US") == "AH"

    def test_to_julian(self):
        assert self.hijri_obj.to_julian() == 2447961

    def test_to_gregorian(self):
        assert self.hijri_obj.to_gregorian().datetuple() == (1990, 3, 10)

    def test_month_index(self):
        assert self.hijri_obj._month_index() == 811

    @pytest.mark.parametrize(
        "test_input", [(1410, 9, 30), (1356, 1, 1), (1500, 12, 30)]
    )
    def test_valid_date(self, test_input):
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
        ],
    )
    def test_invalid_year(self, test_input, expected):
        with pytest.raises(OverflowError) as e:
            convert.Hijri(*test_input, validate=False)._check_date()
        assert str(e.value) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ((1410, 0, 1), "month must be in 1..12"),
            ((1410, 13, 1), "month must be in 1..12"),
            ((1410, 8, 30), "day must be in 1..29 for month"),
        ],
    )
    def test_invalid_day_or_month(self, test_input, expected):
        with pytest.raises(ValueError) as e:
            convert.Hijri(*test_input, validate=False)._check_date()
        assert str(e.value) == expected


@pytest.fixture(scope="class")
def gregorian_obj(request):
    request.cls.gregorian_obj = convert.Gregorian(1990, 3, 10)


@pytest.mark.usefixtures("gregorian_obj")
class TestGregorian:
    def test_fromdate(self):
        test_date = date(2014, 12, 28)
        assert convert.Gregorian.fromdate(test_date).datetuple() == (2014, 12, 28)

    def test_datetuple(self):
        assert self.gregorian_obj.datetuple() == (1990, 3, 10)

    def test_dmyformat(self):
        assert self.gregorian_obj.dmyformat() == "10/03/1990"
        assert self.gregorian_obj.dmyformat(padding=False) == "10/3/1990"
        assert self.gregorian_obj.dmyformat(separator=".") == "10.03.1990"

    def test_month_name(self):
        assert self.gregorian_obj.month_name() == "March"
        assert self.gregorian_obj.month_name("en") == "March"
        assert self.gregorian_obj.month_name("en-US") == "March"

    def test_day_name(self):
        assert self.gregorian_obj.day_name() == "Saturday"
        assert self.gregorian_obj.day_name("en") == "Saturday"
        assert self.gregorian_obj.day_name("en-US") == "Saturday"

    def test_notation(self):
        assert self.gregorian_obj.notation() == "CE"
        assert self.gregorian_obj.notation("en") == "CE"
        assert self.gregorian_obj.notation("en-US") == "CE"

    def test_to_julian(self):
        assert self.gregorian_obj.to_julian() == 2447961

    def test_to_hijri(self):
        assert self.gregorian_obj.to_hijri().datetuple() == (1410, 8, 13)

    @pytest.mark.parametrize(
        "test_input", [(1990, 3, 10), (1924, 8, 1), (2077, 11, 16)]
    )
    def test_valid_range(self, test_input):
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
    def test_invalid_range(self, test_input, expected):
        with pytest.raises(OverflowError) as e:
            convert.Gregorian(*test_input)._check_range()
        assert str(e.value) == expected
