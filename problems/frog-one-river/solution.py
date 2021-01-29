#!/bin/python3


def solution(x, a):
    s = set()
    
    for time, position in enumerate(a):
        if position not in s:
            s.add(position)
        
        if len(s) == x:
            return time
    
    return -1
        
        
if __name__ == '__main__':
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
