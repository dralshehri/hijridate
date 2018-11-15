import pytest
from hijriconverter import convert
from os import path
import json


def load_params_from_json():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, "fixtures", "month_starts.json")) as f:
        loaded = [[tuple(i) for i in x] for x in json.load(f)]
        hijri_gregorian = [tuple(x) for x in loaded]
        gregorian_hijri = [tuple(x[::-1]) for x in loaded]
        return hijri_gregorian, gregorian_hijri


hijri_gregorian_params, gregorian_hijri_params = load_params_from_json()


@pytest.mark.parametrize("test_input, expected", hijri_gregorian_params)
def test_convert_hijri_to_gregorian(test_input, expected):
    year, month, day, calendar = test_input
    hijri = convert.Hijri(year, month, day, calendar)
    converted = hijri.to_gregorian().timetuple()[:3]
    assert converted == expected


@pytest.mark.parametrize("test_input, expected", gregorian_hijri_params)
def test_convert_gregorian_to_hijri(test_input, expected):
    year, month, day = test_input
    gregorian = convert.Gregorian(year, month, day)
    converted = gregorian.to_hijri(expected[3]).datetuple()
    assert converted == expected[:3]
