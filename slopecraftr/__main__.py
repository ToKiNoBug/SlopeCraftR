import sys
from argparse import ArgumentParser

from slopecraftr import constants, cli, gui
from slopecraftr.utils import Version


def environment_check():
    python_version = Version(
        major=sys.version_info.major,
        minor=sys.version_info.minor,
        patch=sys.version_info.micro
    )

    if python_version < constants.REQUIRES_PYTHON:
        raise RuntimeWarning(
            f'Python {python_version} is too old, '
            f'at least {constants.REQUIRES_PYTHON} is required'
        )


def main(*args: str):
    environment_check()
    parser = ArgumentParser(
        prog=constants.PACKAGE_NAME,
        description=constants.NAME
    )
    parser.add_argument('-v', '--version', action='version', version=f'{constants.NAME} v{constants.VERSION}')
    subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser')
    subparsers.add_parser('gui', help='Start GUI')

    parser_cli = subparsers.add_parser('cli', help='Start GUI')
    parser_cli.add_argument('-l', '--language', )
    parser_cli.add_argument('-i', '--input-pic', )
    parser_cli.add_argument('-o', '--output-dir', )
    parser_cli.add_argument('-s', '--color-space', )
    parser_cli.add_argument('-t', '--block-table', )

    subparsers_cli = parser_cli.add_subparsers(title='Options', dest='subparser_cli')
    parser_cli_out = subparsers_cli.add_parser('out', help='Output Formats')
    parser_cli_out.add_argument('--map')
    parser_cli_out.add_argument('--structure-block')
    parser_cli_out.add_argument('--worldedit')
    parser_cli_out.add_argument('--litematica')

    result = parser.parse_args(args)

    if result.subparser == 'cli':
        cli.entry()
    elif result.subparser == 'gui':
        gui.entry()
    else:
        parser.print_help()


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
