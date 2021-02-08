#!/bin/python3

"""
Time complexity: O(n)
Space complexity: O(1)
"""


def sort_colors(colors: list[int]) -> list[int]:
    red_counter = 0
    white_counter = 0
    blue_counter = 0

    for color in colors:
        if color == 0:
            red_counter += 1
        elif color == 1:
            white_counter += 1
        else:
            blue_counter += 1

    colors[:red_counter] = [0] * red_counter
    colors[red_counter:red_counter + white_counter] = [1] * white_counter
    colors[red_counter + white_counter:red_counter + white_counter + blue_counter] = [2] * blue_counter
    return colors


if __name__ == '__main__':
    print(sort_colors([2, 0, 2, 1, 1, 0]))
