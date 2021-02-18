import unittest

from battleships_in_a_board import battleships_in_a_board_naive, battleships_in_a_board


class TestBattleshipsInABoard(unittest.TestCase):
    def test_naive(self):
        board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
        self.assertEqual(battleships_in_a_board_naive(board), 2)

    def test_battelships(self):
        board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
        self.assertEqual(battleships_in_a_board(board), 2)