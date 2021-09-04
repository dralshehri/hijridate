import json
from pathlib import Path

import pytest

from hijri_converter import Gregorian, Hijri


def load_params_from_json():
    data = []
    files = Path(__file__).parent.joinpath("fixtures").glob("*.json")
    for file in files:
        file_content = json.loads(file.read_text())
        # skip test data when the last element is False
        file_data = [
            [tuple(i) for i in x[0]] for x in file_content if x[-1] is not False
        ]
        data += file_data
    params = [tuple(x) for x in data]
    params_reversed = [tuple(x[::-1]) for x in data]
    return params, params_reversed


hijri_gregorian_params, gregorian_hijri_params = load_params_from_json()


@pytest.mark.parametrize("test_input, expected", hijri_gregorian_params)
def test_convert_hijri_to_gregorian(test_input, expected):
    year, month, day = test_input
    hijri = Hijri(year, month, day, validate=False)
    converted = hijri.to_gregorian().datetuple()
    assert converted == expected


@pytest.mark.parametrize("test_input, expected", gregorian_hijri_params)
def test_convert_gregorian_to_hijri(test_input, expected):
    year, month, day = test_input
    gregorian = Gregorian(year, month, day)
    converted = gregorian.to_hijri().datetuple()
    assert converted == expected
