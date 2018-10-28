from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'CHANGELOG.rst'), encoding='utf-8') as f:
    long_description += '\n' + f.read()

setup(
    name='hijriconverter',
    version='1.0.0',
    description='Convert Hijri to/from Gregorian using Umm al-Qura calendar',
    long_description=long_description,
    url='https://github.com/dralshehri/hijri-converter',
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
