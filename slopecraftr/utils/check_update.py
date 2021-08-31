import requests

from slopecraftr import constants

if __name__ == '__main__':
    print(requests.get(constants.GITHUB_API))
