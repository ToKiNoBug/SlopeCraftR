import unittest

from slopecraftr import utils


class TranslationTest(unittest.TestCase):
    def test_num(self):
        self.assertEqual(utils.tr(), None)


if __name__ == '__main__':
    unittest.main()
