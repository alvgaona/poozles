import unittest

from add_strings import add_strings


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        self.assertEqual(add_strings('1', '10'), '11')
        self.assertEqual(add_strings('9', '99'), '108')
        self.assertEqual(add_strings('123', '123'), '246')