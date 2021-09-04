import sys

from slopecraftr.__main__ import main

if __name__ == '__main__':
    sys.exit(main('gui', *sys.argv[1:]))
