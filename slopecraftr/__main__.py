import sys

from semver import VersionInfo

from slopecraftr import constants, cli, gui


def environment_check():
    python_version = VersionInfo(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro
    )

    if python_version < constants.PYTHON_REQUIRED:
        raise RuntimeWarning(
            f'Python {python_version} is too old, '
            f'at least {constants.PYTHON_REQUIRED} is required'
        )


def main():
    environment_check()
    print(
        f'# {constants.NAME} v{constants.VERSION} is starting up',
        f'# {constants.NAME} is open source at {constants.REPOSITORY}',
        f'# {constants.NAME} is on developing, it may have many bugs',
        sep='\n', end='\n' * 2
    )

    if __name__ == '__main__':
        print(
            f'Use command:',
            f'- `python -m {cli.__name__}` for CLI',
            f'- `python -m {gui.__name__}` for GUI',
            sep='\n'
        )


if __name__ == '__main__':
    sys.exit(main())