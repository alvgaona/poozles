# https://leetcode.com/problems/remove-element

def remove_element(nums: list[int], val: int) -> int:
    lastNonTargetAt = 0
    
    for cur in range(0, len(nums)):
        if nums[cur] != val:
            tmp = nums[cur]
            nums[cur] = nums[lastNonTargetAt]
            nums[lastNonTargetAt] = tmp
            lastNonTargetAt += 1
    
    return lastNonTargetAt
