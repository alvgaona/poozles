import unittest

from cyclic_rotation import cyclic_rotation


class TestCyclicRotation(unittest.TestCase):
    def test_cyclic_rotation(self):
        array = [1, 2, 3, 4]
        cyclic_rotation(array, 2)
        self.assertEqual(array, [3, 4, 1, 2])
