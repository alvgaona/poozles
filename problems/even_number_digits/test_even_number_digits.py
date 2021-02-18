import unittest

from even_number_digits import even_number_digits


class TestEvenNumerDigits(unittest.TestCase):
    def test_even_number_digits(self):
        self.assertEqual(even_number_digits([12, 345, 2, 6, 7896]), 2)