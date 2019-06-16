import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent
readme = (here / "README.rst").read_text(encoding="utf-8")
changelog = (here / "CHANGELOG.rst").read_text(encoding="utf-8")

setup(
    name="hijri-converter",
    version="2.1.0",
    description="Accurate Hijri-Gregorian date converter based on the "
    "Umm al-Qura calendar",
    long_description="\n".join([readme, changelog]),
    long_description_content_type="text/x-rst",
    url="https://github.com/dralshehri/hijri-converter",
    project_urls={"Documentation": "https://hijri-converter.readthedocs.io/"},
    author="Mohammed Alshehri",
    author_email="",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Utilities",
    ],
    keywords="hijri gregorian date converter ummalqura saudi calendar",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
)
