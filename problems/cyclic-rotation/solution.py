from math import floor


# Assumptions:
# N, K in [0, 100]
# Each integer in A is in [-1000, 1000]
# Time complexity is about O(n) and space complexity O(1).
def solution(A, k):
    n = len(A)

    if k == 0 or n == 0:
        return A
    
    reverse(A, (0, n))
    reverse(A, (0, k % n))
    reverse(A, (k % n, n))
    
    return A


# Parameters:
#   input: list
#   limits: limits of the list in which to apply reverse upon (e. g. [0, 7))
# Time and space complexity:
#   The time complexity is O(n/2).
#   The space complexity is O(1) as we reverse the list in-place.
def reverse(input, limits):
    if len(input) < 2:
        return
    
    rng = floor((limits[1] - limits[0]) / 2)
    
    head = limits[0]
    tail = limits[1] - 1
    
    for index in range(0, rng):
        aux = input[head + index]
        input[head + index] = input[tail - index]
        input[tail - index] = aux


if __name__ == '__main__':
    input = []
    solution(input, 3)
    print(input)
