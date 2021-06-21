# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../src/hijri_converter"))

#
# -- Project information -----------------------------------------------------
#

project = "Hijri Converter"
author = "Mohammed Alshehri"
project_copyright = "2018 Mohammed Alshehri (@dralshehri) and contributors"

#
# -- General configuration -------------------------------------------------------------
#
extensions = [
    "sphinx.ext.autodoc",
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
    "special-members": "__init__",
    "show_inheritance": True,
    "noindex": True,
}

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
html_baseurl = "https://hijri-converter.readthedocs.io/en/stable/"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
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
