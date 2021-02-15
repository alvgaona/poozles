# https://leetcode.com/problems/battleships-in-a-board

def battleships_in_a_board_naive(board: list[list[str]]) -> int:
    def sink(y: int, x: int, board: list[list[str]]) -> None:
        if y >= len(board) or x >= len(board[0]) or board[y][x] == '.':
            return

        sink(y + 1, x, board)
        sink(y, x + 1, board)
        board[y][x] = '.'

    num_battleships = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '.':
                continue
            sink(y, x, board)
            num_battleships += 1

    return num_battleships


def battleships_in_a_board(board: list[list[str]]) -> int:
    num_battleships = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '.' or y > 0 and board[y - 1][x] == 'X' or x > 0 and board[y][x - 1] == 'X':
                continue
            num_battleships += 1

    return num_battleships
