import unittest

from slopecraftr.utils.translation_manager import TranslationManager


class TranslationTest(unittest.TestCase):
    tr = TranslationManager()
    tr.languages_storage = {
        'en_us': tr.expand_dict({
            'info': {
                'author': 'Van_Nya',
                'name': 'SlopeCraftR'
            }
        }),
        'zh_cn': tr.expand_dict({
            'info': {
                'author': 'Van喵喵',
                'name': 'SlopeCraftR'
            }
        })
    }

    def test_tr(self):
        self.assertEqual(self.tr('info.author'), 'Van_Nya')
        self.assertEqual(self.tr('info.author', lang='en_us'), 'Van_Nya')
        self.assertEqual(self.tr('info.author', lang='zh_cn'), 'Van喵喵')
        self.assertEqual(self.tr('info.author', lang='None'), 'Van_Nya')

        self.assertEqual(self.tr('info.name'), self.tr('info.name', lang='en_us'))
        self.assertEqual(self.tr('info.name', lang='en_us'), self.tr('info.name', lang='zh_cn'))
        self.assertEqual(self.tr('info.name', lang='en_us'), self.tr('info.name', lang='None'))


if __name__ == '__main__':
    unittest.main()
