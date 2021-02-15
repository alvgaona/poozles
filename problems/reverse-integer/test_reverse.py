import unittest
from reverse import reverse


class TestReverse(unittest.TestCase):
    def test_reverse(self):
        x = 123
        y = reverse(x)

        self.assertEqual(y, 321)

    def test_unbounded(self):
        x = 1534236469
        y = reverse(x)

        self.assertEqual(y, 0)
