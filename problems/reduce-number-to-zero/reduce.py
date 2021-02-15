# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

def reduce(num: int) -> int:
    """
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    result = num
    counter = 0
    while result != 0:
        result = result / 2 if result % 2 == 0 else result - 1
        counter += 1

    return counter
