# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re
import sys
from pathlib import Path

# Set package variables and add to path
package_name = "hijri_converter"
package_path = Path("../src").joinpath(package_name).resolve()
sys.path.append(str(package_path.parent))


def read_version():
    content = package_path.joinpath("__init__.py").read_text()
    pattern = re.compile(r"(?<=__version__\s=\s\").*(?=\")")
    return pattern.search(content).group()


# Add custom extensions to path
sys.path.append(str(Path("_extensions").resolve()))

#
# -- Project information ---------------------------------------------------------------
#
project = "hijri-converter"  # project name at PyPI and GitHub
author = "Mohammed Alshehri"
project_copyright = "2018 Mohammed Alshehri (https://www.dralshehri.com)"
version = read_version()

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
]

exclude_patterns = ["manpage.*"]
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
pygments_style = "colorful"
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
autoclass_content = "both"
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
html_baseurl = f"https://{project}.readthedocs.io/en/stable/"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "navigation_depth": 1,
    "includehidden": True,
    "titles_only": True,
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
man_pages = [
    ("manpage", package_name, "convert Hijri-Gregorian dates", author, 7)
]
