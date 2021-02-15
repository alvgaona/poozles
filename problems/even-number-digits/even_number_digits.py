#!/usr/bin/python3

from typing import NoReturn
from math import log10


def even_number_digits(nums: list[int]) -> int:
    result = 0
    
    for num in nums:
        if int(log10(num) + 1) % 2 == 0:
            result += 1
    
    return result


def main() -> NoReturn:
    nums = [12, 345, 2, 6, 7896]
    
    assert even_number_digits(nums) == 2


if __name__ == '__main__':
    exit(main())
