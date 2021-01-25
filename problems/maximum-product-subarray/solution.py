#!/usr/bin/python3

# Time complexity is O(n^2) and space complexity O(1)
def brute_force_solution(nums):
    max_product = 0
    start = 0
    end = 0
    for i in range(0, len(nums)):
        aux = 1
        
        for j in range(i, len(nums)):
            aux *= nums[j]
        
        if aux > max_product:
            max_product = aux
            start = i
            end = j
    
    print("Found maximum subarray between {} and {}".format(start, end))
    return max_product


# Time complexity is O(n) and space complexity O(1)
def optimized_solution(nums):
    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0
    
    for i in range(0, len(nums)):
        if nums[i] > max_ending_here * nums[i]:
            start = i
            max_ending_here = nums[i]
        else:
            max_ending_here *= nums[i]
            
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = i
    
    print("Found maximum subarray between {} and {}".format(start, end))
    return max_so_far
        
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    
    assert brute_force_solution(nums) == 24
    assert optimized_solution(nums) == 24
