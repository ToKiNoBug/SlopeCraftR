import os

from setuptools import find_packages, setup

from slopecraftr import constants

NAME = constants.PACKAGE_NAME
VERSION = str(constants.VERSION)
DESCRIPTION = constants.DESCRIPTION
URL = constants.REPOSITORY
AUTHOR = constants.AUTHOR
LICENSE = constants.LICENSE
REQUIRES_PYTHON = f'>={constants.PYTHON_REQUIRED}'

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
    license=LICENSE,
    classifiers=CLASSIFIERS,
)
