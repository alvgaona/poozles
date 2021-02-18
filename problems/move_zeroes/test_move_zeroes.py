import unittest


from move_zeroes import move_zeroes, move_zeroes_optimized


class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes_naive(self):
        items = [
            ([0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0]),
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]),
            ([], []),
            ([99, 0, 0, 0], [99, 0, 0, 0])
        ]
        
        for item in items:
            self.assertEqual(move_zeroes(item[0]), item[1])
