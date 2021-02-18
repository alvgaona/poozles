import unittest

from roman_to_integer import roman_to_integer


class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_integer(self):
        self.assertEqual(roman_to_integer('III'), 3)
        self.assertEqual(roman_to_integer('IV'), 4)
        self.assertEqual(roman_to_integer('LVIII'), 58)
        self.assertEqual(roman_to_integer('MCMXCIV'), 1994)

