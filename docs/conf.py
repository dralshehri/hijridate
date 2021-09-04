# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re
import sys
from pathlib import Path

package_name = "hijri_converter"
package_path = Path("../src").joinpath(package_name)
sys.path.append(str(package_path.resolve()))


#
# -- Project information -----------------------------------------------------
#
project = "Hijri Converter"
author = "Mohammed Alshehri (@dralshehri)"
project_copyright = "2018 Mohammed Alshehri (@dralshehri) and contributors"

init_file_content = package_path.joinpath("__init__.py").read_text()
version = re.search(r"(?<=__version__\s=\s\").*(?=\")", init_file_content).group()

#
# -- General configuration -------------------------------------------------------------
#
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "notfound.extension",
]
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
pygments_style = "colorful"

#
# -- Options for autodoc -------------------------------------------------
#
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": False,
    "show_inheritance": True,
}
autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_mock_imports = [package_name]
autodoc_typehints = "signature"

#
# -- Options for intersphinx -------------------------------------------------
#
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

#
# -- Options for notfound -------------------------------------------------
#
notfound_urls_prefix = "/en/stable/"

#
# -- Options for Markdown files --------------------------------------------------------
#
myst_enable_extensions = [
    "colon_fence",
    "smartquotes",
]
myst_heading_anchors = 2

#
# -- Options for HTML output -----------------------------------------------------------
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "navigation_depth": 1,
    "includehidden": True,
    "titles_only": True,
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False

#
# -- Options for manual pages output -----------------------------------------------------------
#
man_pages = [
    ("man", package_name, "Umm al-Qura Hijri-Gregorian dates converter", author, 7)
]
