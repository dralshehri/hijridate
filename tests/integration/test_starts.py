import pytest
from hijriconverter import convert
import pathlib
import json


def load_params_from_json():
    fixtures = pathlib.Path(__file__).parent.joinpath("fixtures")
    file_content = (fixtures / "month_starts.json").read_text()
    data = [[tuple(i) for i in x] for x in json.loads(file_content)]
    params = [tuple(x) for x in data]
    params_reversed = [tuple(x[::-1]) for x in data]
    return params, params_reversed


hijri_gregorian_params, gregorian_hijri_params = load_params_from_json()


@pytest.mark.parametrize("test_input, expected", hijri_gregorian_params)
def test_convert_hijri_to_gregorian(test_input, expected):
    year, month, day = test_input
    hijri = convert.Hijri(year, month, day)
    converted = hijri.to_gregorian().datetuple()
    assert converted == expected


@pytest.mark.parametrize("test_input, expected", gregorian_hijri_params)
def test_convert_gregorian_to_hijri(test_input, expected):
    year, month, day = test_input
    gregorian = convert.Gregorian(year, month, day)
    converted = gregorian.to_hijri().datetuple()
    assert converted == expected
