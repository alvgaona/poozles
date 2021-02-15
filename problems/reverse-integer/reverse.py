#!/usr/bin/python3


def reverse(x: int) -> int:
    """
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    result = 0
    num = abs(x)

    while num > 0:
        result = result * 10 + num % 10
        num = int(num / 10)

    if result < -2 ** 31 or result > 2 ** 31 - 1:
        return 0

    return -1 * result if x < 0 else result
