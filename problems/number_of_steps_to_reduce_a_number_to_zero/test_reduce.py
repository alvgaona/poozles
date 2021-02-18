import unittest

from reduce import reduce


class TestReduceNumberToZero(unittest.TestCase):
    def test_reduce(self):
        self.assertEqual(reduce(14), 6)
