import unittest

from sort_colors import sort_colors


class TestSortColors(unittest.TestCase):
    def test_sort_colors(self):
        self.assertEqual(sort_colors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])
