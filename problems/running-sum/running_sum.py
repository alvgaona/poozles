#!/usr/bin/python3

def running_sum(nums: list[int]) -> list[int]:
    L = len(nums)
    
    sum = [0] * L
    
    for i in range(0, L):
        if i == 0:
            sum[i] = nums[i]
        else:
            sum[i] = sum[i - 1] + nums[i]
    
    return sum


def main() -> None:
    nums = [1, 2, 3, 4, 5]
    
    assert running_sum(nums) == [1, 3, 6, 10, 15]


if __name__ == '__main__':
    exit(main())
