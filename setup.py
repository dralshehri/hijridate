"""Setup.py entry point for supporting editable installs

Configuration is handled by setuptools through setup.cfg
https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import re
from pathlib import Path

import setuptools

# Clean the readme file from badges and markers
this_directory = Path(__file__).parent
readme_content = (this_directory / "README.md").read_text()
readme_content_no_badges = re.sub(
    r"<!-- start badges -->[\S\s]+<!-- end badges -->\n+",
    "",
    readme_content,
)
readme_content_cleaned = re.sub(
    r"(<!-- .* -->)\n+", "", readme_content_no_badges
)

# Package name is added here for GitHub's dependency graph
# Also, a cleaner version of the long description is added
setuptools.setup(
    name="hijri-converter",
    long_description=readme_content_cleaned,
    long_description_content_type="text/markdown",
)
