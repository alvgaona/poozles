# https://leetcode.com/problems/number-of-island


def number_of_islands(grid: list[list[str]]) -> int:
    def check(y: int, x: int, grid: list[list[str]]) -> None:
        if y >= len(grid) or y < 0 or x < 0 or x >= len(grid[0]) or grid[y][x] == '0':
            return

        grid[y][x] = '0'
        check(y + 1, x, grid)
        check(y, x + 1, grid)
        check(y - 1, x, grid)
        check(y, x - 1, grid)


    num_islands = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '0':
                continue
            check(y, x, grid)
            num_islands += 1

    return num_islands
