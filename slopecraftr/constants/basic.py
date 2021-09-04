from slopecraftr.utils import Version, PreRelease

# Names
NAME = 'SlopeCraftR'
PACKAGE_NAME = NAME.lower()

# Version Info
VERSION = Version(
    major=0,
    minor=1,
    patch=0,
    prerelease=PreRelease().alpha(5)
)
NEXT_VERSION = Version(
    major=0,
    minor=1,
    patch=0,
    prerelease=PreRelease().beta(1)
)
REQUIRES_PYTHON = Version(
    major=3,
    minor=8
)

# Author Info
AUTHOR = 'Van_Nya'
AUTHOR_EMAIL = 'nya@ruavan.one'

# Project Info
REPOSITORY_URL = 'https://github.com/Van-Nya/SlopeCraftR'
GITHUB_API = 'https://api.github.com/repos/Van-Nya/SlopeCraftR/releases/latest'
DESCRIPTION = 'Get your 3D map pixel art in minecraft'
LICENSE = 'GPL-3.0'
