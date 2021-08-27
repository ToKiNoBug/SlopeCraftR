from slopecraftr.constants.basic import *

__all__ = [
    # basic
    'NAME', 'PACKAGE_NAME',
    'VERSION', 'PYTHON_REQUIRED',
    'AUTHOR', 'REPOSITORY', 'DESCRIPTION'
]

if __name__ == '__main__':
    from inspect import getmembers
    from slopecraftr.constants import basic
    members = dict(getmembers(basic))
    for _ in __all__:
        print(f'{_}: {members[_]}')
