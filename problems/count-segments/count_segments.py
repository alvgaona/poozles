# https://leetcode.com/problems/number-of-segments-in-a-string


def count_segments(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    count = 0

    for i in range(0, len(s)):
        if ord(s[i]) != 32 and (i + 1 == len(s) or ord(s[i + 1]) == 32):
            count += 1

    return count
