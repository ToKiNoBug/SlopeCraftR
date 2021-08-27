import sys
from argparse import ArgumentParser
from getpass import getpass

from slopecraftr import constants
from slopecraftr.__main__ import main as scr_main


def cli_entry():
    parser = ArgumentParser(
        prog=constants.PACKAGE_NAME,
        description=f'{constants.NAME}-CLI'
    )
    parser.add_argument('-q', '--quiet', help='Disable CLI output', action='store_true')

    quiet = (result := parser.parse_args()).quiet
    print(parser, result, quiet, sep='\n', end='\n' * 2)


def main():
    scr_main()
    print(f'<{constants.NAME}-CLI>', end='\n' * 2)
    cli_entry()


if __name__ == '__main__':
    sys.exit(main())
