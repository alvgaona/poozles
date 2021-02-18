# https://leetcode.com/problems/find-numbers-with-even-number-of-digits

from math import log10


def even_number_digits(nums: list[int]) -> int:
    result = 0
    
    for num in nums:
        if int(log10(num) + 1) % 2 == 0:
            result += 1
    
    return result
