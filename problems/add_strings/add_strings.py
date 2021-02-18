# https://leetcode.com/problems/add-strings


def add_strings(num1: str, num2: str) -> str:
    """
    Time complexity: O(L)
    Space complexity: O(L)
    """
    P = len(num1)
    Q = len(num2)
    L = max(P, Q)

    if L >= 5100:
        raise ValueError('Input exceed maximum admissible length')

    carry = 0
    output = ""

    for i in range(0, L):
        d1 = 48 if i > P - 1 else ord(num1[P - 1 - i])
        d2 = 48 if i > Q - 1 else ord(num2[Q - 1 - i])

        sum = (d1 + d2) % 48

        r = sum % 10 + carry if carry != 0 else sum % 10

        carry = int(sum / 10) + int(r / 10)

        output = chr(ord('0') + r % 10) + output

    if carry != 0:
        output = chr(ord('0') + carry) + output

    return output
