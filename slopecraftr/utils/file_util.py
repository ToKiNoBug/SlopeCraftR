import os
from typing import Callable, List
from functools import partial


def list_all(directory: str, _filter: Callable[[str], bool] = lambda file_path: True) -> List[str]:
    return list(filter(_filter, map(partial(os.path.join, directory), os.listdir(directory))))


def list_file(directory: str, _filter: Callable[[str], bool] = lambda file_path: True) -> List[str]:
    return list_all(directory, lambda file_path: os.path.isfile(file_path) and _filter(file_path))


def list_file_with_suffix(directory: str, suffix: str) -> List[str]:
    return list_file(directory, lambda file_path: file_path.endswith(suffix))


def touch_directory(directory_path: str):
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
