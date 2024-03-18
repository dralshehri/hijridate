"""Configuration file for the Sphinx documentation builder.

Full list of options can be found in the Sphinx documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import re
import sys

from pathlib import Path

# Set package name and path
package_name = "hijridate"
package_path = Path("../src").joinpath(package_name).resolve()
sys.path.append(str(package_path.parent))


def get_version():
    """Return the current version of the package."""
    content = package_path.joinpath("__init__.py").read_text()
    pattern = re.compile(r"(?<=__version__\s=\s\").*(?=\")")
    return pattern.search(content).group()


# Add custom extensions to path
sys.path.append(str(Path("_ext").resolve()))

#
# -- Project information ---------------------------------------------------------------
#
project = "HijriDate"  # project name at PyPI and GitHub
author = "Mohammed Alshehri"
project_copyright = "2018 Mohammed Alshehri"
version = get_version()

#
# -- General configuration -------------------------------------------------------------
#
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "myst_parser",
    "notfound.extension",
    "custom_sitemap",
    "custom_manpage",
]

exclude_patterns = ["manpage.*"]
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
pygments_style = "sphinx"
pygments_dark_style = "monokai"
add_module_names = False

#
# -- Options for autodoc ---------------------------------------------------------------
#
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": False,
    "show-inheritance": True,
}
autoclass_content = "class"
autodoc_typehints = "description"

#
# -- Options for intersphinx -----------------------------------------------------------
#
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

#
# -- Options for napoleon -----------------------------------------------------------
#
napoleon_google_docstring = True
napoleon_numpy_docstring = False

#
# -- Options for notfound --------------------------------------------------------------
#
notfound_urls_prefix = "/en/stable/"

#
# -- Options for sitemap ---------------------------------------------------------------
#
sitemap_excluded_pages = [
    "contributing",
    "license",
]

#
# -- Options for Markdown files --------------------------------------------------------
#
myst_enable_extensions = [
    "smartquotes",
]
myst_heading_anchors = 2

#
# -- Options for HTML output -----------------------------------------------------------
#
html_baseurl = f"https://{package_name}.readthedocs.io/en/stable/"
html_title = f"{project} Documentation"
html_theme = "furo"
html_theme_options = {
    "top_of_page_button": None,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/dralshehri/hijridate",
            "html": '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>',  # noqa: E501
            "class": "",
        },
    ],
}
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}
html_logo = None
html_favicon = None
html_css_files = ["custom.css"]
html_static_path = ["_static"]
html_extra_path = ["_extra"]
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False

#
# -- Options for manual pages output ---------------------------------------------------
#
man_pages = [("manpage", package_name, "convert Hijri-Gregorian dates", author, 7)]
