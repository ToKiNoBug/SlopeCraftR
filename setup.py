import os

from setuptools import find_packages, setup

from slopecraftr import constants

NAME = constants.PACKAGE_NAME
VERSION = str(constants.SEMVER)
DESCRIPTION = 'Get your 3D map pixel art in minecraft'
URL = 'https://github.com/Van-Nya-Stew/SlopeCraft'
AUTHOR = 'Van_Nya'
REQUIRES_PYTHON = '>=3.8.0'

CLASSIFIERS = [
    # https://pypi.org/classifiers/
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Operating System :: OS Independent'
]

# ----------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIRED = [line for line in f.readlines() if not len(line.strip()) == 0]

print(f'REQUIRED = {REQUIRED}')

with open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=[]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='LGPL-3.0',
    classifiers=CLASSIFIERS,
)
