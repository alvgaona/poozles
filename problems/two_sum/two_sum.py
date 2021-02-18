# https://leetcode.com/problems/two-sum

def two_sum(nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for index, value in enumerate(nums):
        complement = target - value

        complement_index = nums_map.get(complement)

        if complement_index is not None:
            return [complement_index, index]

        nums_map[value] = index

    raise ValueError('There is no solution')
