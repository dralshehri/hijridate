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
project_copyright = "2018 Mohammed Alshehri (@dralshehri)"
author = "Mohammed Alshehri"

#
# -- General configuration -------------------------------------------------------------
#
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "myst_parser",
]
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

#
# -- Options for autodoc -------------------------------------------------
#
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "inherited-members": True,
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
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}
html_theme_options = {
    "light_css_variables": {
        "code-font-size": "var(--font-size--small)",
        "color-foreground-primary": "#24292e",
        "color-foreground-muted": "#868e96",
        "color-foreground-border": "#868e96",
        "color-background-secondary": "#f1f3f5",
        "color-background-border": "#e9ecef",
        "color-brand-primary": "#1971c2",
        "color-brand-content": "#1971c2",
    },
}
