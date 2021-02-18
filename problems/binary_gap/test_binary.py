import unittest
from binary import binary


class TestBinary(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(binary(8), [1, 0, 0, 0])