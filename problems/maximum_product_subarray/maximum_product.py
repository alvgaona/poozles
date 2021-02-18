# https://leetcode.com/problems/maximum-product-subarray/

# Time complexity is O(n^2) and space complexity O(1)
def maximum_product_bf(nums: list[int]) -> (int, int, int):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
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
    
    return max_product, start, end


def maximum_product_opt(nums: list[int]) -> (int, int, int):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
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
    
    return max_so_far, start, end
