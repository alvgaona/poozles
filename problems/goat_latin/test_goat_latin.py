import unittest

from goat_latin import to_goat_latin


class TestGoatLatin(unittest.TestCase):
    def test_goat_latin(self):
        self.assertEqual(
            to_goat_latin('The quick brown fox jumped over the lazy dog'),
            'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
        )
