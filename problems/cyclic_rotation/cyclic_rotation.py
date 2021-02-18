# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation

from typing import Union, Any
from math import floor


def cyclic_rotation(array: list[int], k: int):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    n = len(array)
    
    if k == 0 or n == 0:
        return array
    
    reverse(array, (0, n))
    reverse(array, (0, k % n))
    reverse(array, (k % n, n))
    

def reverse(array: list[int], limits: tuple[Union[int, Any], int]):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if len(array) < 2:
        return
    
    rng = floor((limits[1] - limits[0]) / 2)
    
    head = limits[0]
    tail = limits[1] - 1
    
    for index in range(0, rng):
        aux = array[head + index]
        array[head + index] = array[tail - index]
        array[tail - index] = aux
