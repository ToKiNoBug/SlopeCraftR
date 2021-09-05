import os
from random import choice

from ruamel import yaml
from slopecraftr import constants
from slopecraftr.utils.types import TranslationStorageDict, LanguagesStorageDict
from slopecraftr.utils.file_util import list_file_with_suffix

LANGUAGE_PATH = os.path.join(constants.PACKAGE_PATH, 'resources', 'lang')


class TranslationManager:
    def __init__(self):
        self.languages_storage: LanguagesStorageDict = dict()
        for lang_file in list_file_with_suffix(LANGUAGE_PATH, constants.LANGUAGE_FILE_SUFFIX):
            with open(os.path.join(LANGUAGE_PATH, f'{lang_file}'), encoding='utf8') as f:
                lang = os.path.basename(lang_file).rsplit('.', 1)[0]
                self.languages_storage[lang] = self.expand_dict(dict(yaml.safe_load(f)))

    def __call__(self, tr_key: str, *, lang: str = constants.DEFAULT_LANGUAGE) -> str:
        """
        Translate key to string in specified language

        :param tr_key: key to translate
        :param lang: defaults to en_us
        :return: translated key if tr_key exists else tr_key
        """
        _lang = lang.lower()
        is_default = _lang == constants.DEFAULT_LANGUAGE
        default_lang_dict = self.languages_storage[constants.DEFAULT_LANGUAGE]
        return self.languages_storage.get(_lang, default_lang_dict).get(
            tr_key, tr_key if is_default else self(tr_key)
        )

    def __str__(self):
        return yaml.round_trip_dump(self.languages_storage)

    @classmethod
    def expand_dict(cls, _dict: dict, *path: str, sep: str = '.') -> TranslationStorageDict:
        """
        Expand a yaml-format dict to ``dict[str, str]`` type

        :param _dict: dict to expand
        :param path: path of self in the root dict
        :param sep: string inserted between values in path
        :return: dict with single depth
        """
        def expand_list(_list: list):
            res = choice(_list)
            return choice(res) if isinstance(res, list) else res

        result: TranslationStorageDict = dict()
        for key, val in _dict.items():
            key = str(key)
            if isinstance(val, list):
                val = expand_list(val)
            result.update(
                cls.expand_dict(val, key, *path, sep=sep) if isinstance(val, dict)
                else {sep.join([*path, key]): str(val)}
            )
        return result
