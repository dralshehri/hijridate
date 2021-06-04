"""Setup.py entry point for supporting editable installs

Configuration is handled by setuptools through setup.cfg
https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import setuptools

if __name__ == "__main__":
    # Package name is added here for GitHub's dependency graph
    setuptools.setup(name="hijri-converter")
