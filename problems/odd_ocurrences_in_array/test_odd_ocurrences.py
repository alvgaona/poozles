import unittest

from odd_ocurrences import odd_ocurrences


class TestOddOcurrencies(unittest.TestCase):
    def test_odd_ocurrencies(self):
        self.assertEqual(odd_ocurrences([2, 2, 3, 4, 4, 5, 5]), 3)
