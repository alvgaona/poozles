#!/usr/bin/python3

def two_sum(nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for index, value in enumerate(nums):
        complement = target - value

        complement_index = nums_map.get(complement)

        if complement_index is not None:
            return [complement_index, index]

        nums_map[value] = index

    raise ValueError('There is no solution')


if __name__ == '__main__':
    test_inputs = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    for test_input in test_inputs:
        numbers, target, expected = test_input
        assert two_sum(numbers, target) == expected
