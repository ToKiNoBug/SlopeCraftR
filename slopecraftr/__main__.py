import sys

from slopecraftr import constants, cli, gui
from slopecraftr.utils import Version


def environment_check():
    python_version = Version(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro
    )

    if python_version < constants.REQUIRES_PYTHON:
        raise RuntimeWarning(
            f'Python {python_version} is too old, '
            f'at least {constants.REQUIRES_PYTHON} is required'
        )


def main():
    environment_check()
    print(
        f'# {constants.NAME} v{constants.VERSION} is starting up',
        f'# {constants.NAME} is open source at {constants.REPOSITORY_URL}',
        f'# {constants.NAME} is on developing, it may have many bugs',
        sep='\n', end='\n' * 2
    )

    if __name__ == '__main__':
        print(
            'Use command:',
            f'- `python -m {cli.__name__}` for CLI',
            f'- `python -m {gui.__name__}` for GUI',
            sep='\n'
        )


if __name__ == '__main__':
    sys.exit(main())
