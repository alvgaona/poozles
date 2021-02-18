import unittest

from jewels_and_stones import jewels_and_stones


class TestJewelsAndStones(unittest.TestCase):
    def test_jewels_and_stones(self):
        self.assertEqual(jewels_and_stones('aA', 'aAAbbbb'), 3)
