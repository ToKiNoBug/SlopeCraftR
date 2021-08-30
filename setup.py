import os
import re

from setuptools import find_packages, setup

from slopecraftr import constants

VERSION = constants.VERSION
REQUIRES_PYTHON = f'>={constants.REQUIRES_PYTHON}'

CLASSIFIERS = [
    # https://pypi.org/classifiers/
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Operating System :: OS Independent'
]

if os.getenv('CI', None) is not None:
    build_num = os.getenv('GITHUB_RUN_NUMBER', None)
    is_release = os.getenv('GITHUB_REF', '').startswith('refs/tags/v')
    if build_num is not None and not is_release:
        VERSION.replace(build=f'build.{build_num}')

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIRED = [line for line in f.readlines() if not len(line.strip()) == 0]

print('REQUIRED:\n', *REQUIRED, sep='- ')

with open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    LONG_DESCRIPTION = re.compile(r'(\n.*<!-- lang -->\n)').sub('', f.read())

# ----------------------------------------------------------------

setup(
    name=constants.NAME,
    version=str(VERSION),
    description=constants.DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=constants.AUTHOR,
    author_email=constants.AUTHOR_EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=constants.REPOSITORY_URL,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    install_requires=REQUIRED,
    include_package_data=True,
    license=constants.LICENSE,
    classifiers=CLASSIFIERS,
)
