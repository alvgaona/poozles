# https://leetcode.com/problems/roman-to-integer

def roman_to_integer(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    subtractions = {
        'I': {'V', 'X'},
        'X': {'L', 'C'},
        'C': {'D', 'M'}
    }

    result = 0

    j = 1
    i = 0
    while i < len(s):
        cur = s[i]
        if j < len(s):
            next = s[j]

            instances = subtractions.get(cur)
            if instances is not None and next in instances:
                result -= mapping[cur]
                i += 1
                j += 1
                continue

        result += mapping[cur]
        i += 1
        j += 1

    return result
