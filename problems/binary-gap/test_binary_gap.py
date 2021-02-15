import unittest

from binary_gap import binary_gap, binary_gap_xor


class TestBinaryGap(unittest.TestCase):
    def test_binary_gap(self):
        self.assertEqual(binary_gap(328), 2)

    def test_binary_gap_xor(self):
        self.assertEqual(binary_gap_xor(328), 2)
