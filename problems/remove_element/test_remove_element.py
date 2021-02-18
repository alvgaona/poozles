import unittest

from remove_element import remove_element


class TestRemoveElement(unittest.TestCase):
    def test_remove_element(self):
        nums = [3, 2, 2, 3]
        val = 3
        self.assertEqual(remove_element(nums, val), [2, 2, 3, 3])
