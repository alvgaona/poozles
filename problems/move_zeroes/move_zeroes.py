# https://leetcode.com/problems/move-zeroes

def move_zeroes(nums: list[int]) -> None:
    head = 0
    for i in range(0, len(nums)):
        if nums[head] == 0:
            nums.pop(head)
            nums.append(0)
            continue
        
        head += 1


def move_zeroes_optimized(nums: list[int]) -> None:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    lastNonZeroFoundAt = 0
    
    for cur in range(0, len(nums)):
        if nums[cur] != 0:
            tmp = nums[cur]
            nums[cur] = nums[lastNonZeroFoundAt]
            nums[lastNonZeroFoundAt] = tmp
            lastNonZeroFoundAt += 1
