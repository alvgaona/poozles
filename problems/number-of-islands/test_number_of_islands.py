import unittest

from number_of_islands import number_of_islands


class TestNumberOfIslands(unittest.TestCase):
    def test_number_of_island_00(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]

        self.assertEqual(number_of_islands(grid), 3)

    def test_number_of_islands_01(self):
        grid = [
            ['1', '1', '1'],
            ['0', '1', '0'],
            ['1', '1', '1']
        ]

        self.assertEqual(number_of_islands(grid), 1)
