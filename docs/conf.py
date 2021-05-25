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
project_copyright = "2018 Mohammed Alshehri (@dralshehri)"
version = "latest"

#
# -- General configuration -------------------------------------------------------------
#
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "myst_parser",
]
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
    # "inherited-members": True,
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
html_baseurl = "https://dralshehri.github.io/hijri-converter/"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'display_version': True,
    'navigation_depth': 1,
    'includehidden': True,
    'titles_only': True,
    'style_nav_header_background': '#2980B9',
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
