from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent
readme = (here / 'README.rst').read_text(encoding='utf-8')

setup(
    name='hijriconverter',
    version='1.2.0',
    description='Convert Hijri to/from Gregorian using Umm al-Qura calendar',
    long_description=readme,
    url='',
    project_urls={
        "Source Code": "https://github.com/dralshehri/hijri-converter",
        "Documentation": "http://hijriconverter.readthedocs.io/en/latest",
    },
    author='Mohammed Alshehri',
    author_email='',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
        'Topic :: Utilities',
    ],
    keywords='hijri date converter ummulqura saudi calendar',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.5',
)
