# https://leetcode.com/problems/sort-colors

def sort_colors(colors: list[int]) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    
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
