import pytest

from hijri_converter import locales


@pytest.fixture(scope="class")
def all_locales(request):
    request.cls.locales = locales._locale_map


@pytest.mark.usefixtures("all_locales")
class TestLocalesValidity:
    def test_locale_data_structure(self):
        for locale_cls in self.locales.values():
            assert len(locale_cls.language_tag) == 2
            assert locale_cls.language_tag.islower()
            assert len(locale_cls.month_names) == 12
            assert all(locale_cls.month_names)  # not blank or None
            assert len(locale_cls.gregorian_month_names) == 12
            assert all(locale_cls.gregorian_month_names)  # not blank or None
            assert len(locale_cls.day_names) == 7
            assert all(locale_cls.day_names)  # not blank or None
            assert locale_cls.notation is not None
            assert locale_cls.gregorian_notation is not None

    def test_locale_map(self):
        assert len(locales._locale_map) > 0
        assert "en" in locales._locale_map.keys()

    def test_duplicated_language_tag(self):
        with pytest.raises(LookupError):

            class ExtraLocale(locales.Locale):
                language_tag = "en"


class TestGettingLocale:
    class CustomLocale(locales.EnglishLocale):
        language_tag = "xx"

    @pytest.mark.parametrize(
        "test_input",
        [
            "xx",
            "XX",
            "xx-YY",
            "xx-yy",
            "xx_yy",
            "xx_YY",
            "xx_YY.UTF-8",
        ],
    )
    def test_locale_possible_names(self, test_input):
        assert locales.get_locale(test_input).__class__ == self.CustomLocale

    def test_unsupported_language(self):
        with pytest.raises(ValueError):
            locales.get_locale("xy")
