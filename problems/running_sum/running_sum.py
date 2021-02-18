# https://leetcode.com/problems/running-sum-of-1d-array

def running_sum(nums: list[int]) -> list[int]:
    L = len(nums)
    
    sum = [0] * L
    
    for i in range(0, L):
        if i == 0:
            sum[i] = nums[i]
        else:
            sum[i] = sum[i - 1] + nums[i]
    
    return sum
