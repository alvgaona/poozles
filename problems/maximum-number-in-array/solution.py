#!/usr/bin/python3

def solution(A):
    maximum = A[0]

    for number in A:
        if number > maximum:
            maximum = number

    return maximum


if __name__ == '__main__':
    A = [299, -15, 48.5, 0.43]

    assert solution(A) == 299
