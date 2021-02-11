#!/bin/python3

def solution(A):
    not_repeated = set()
    repeated = set()
    
    for num in A:
        if num in not_repeated:
            not_repeated.remove(num)
            repeated.add(num)
        else:
            not_repeated.add(num)
    
    return [num for num in not_repeated][0]


if __name__ == '__main__':
    assert solution([2, 2, 3, 4, 4, 5, 5]) == 3
