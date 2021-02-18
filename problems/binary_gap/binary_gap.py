# # https://app.codility.com/programmers/lessons/1-iterations/binary_gap

from binary import binary


def binary_gap(n):
    """
    Time complexity: O(k)
    Space complexity: O(k)

    Where k is the number of digits, k ~ log(n)
    """
    if n > 2 ** 32 / 2 or n < 1:
        return -1

    binary_n = binary(n)

    maximum_gap_length = 0
    gap_length = 0

    for digit in binary_n:
        if digit == 0:
            gap_length += 1
            continue

        if digit == 1:
            if gap_length > maximum_gap_length:
                maximum_gap_length = gap_length

            gap_length = 0

    return maximum_gap_length


def binary_gap_xor(n):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Where n is the number of digits
    """
    if n > 2 ** 32 / 2 or n < 1:
        return -1

    binary_n = binary(n)

    maximum_gap_length = 0
    gap_length = 0

    xor = 0
    for digit in binary_n:
        xor ^= digit

        if xor == 1 and digit == 0:
            gap_length += 1

        if xor == 0 and digit == 1:
            if gap_length > maximum_gap_length:
                maximum_gap_length = gap_length

            gap_length = 0
            xor = 1

    return maximum_gap_length
