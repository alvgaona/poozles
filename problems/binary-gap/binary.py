def int_to_binary(n):
    """
    Time complexity: O(log(n))
    Space complexity: O(log(n))

    Where n is the integer
    """
    if n == 0:
        return [0]

    output = []

    aux = n
    while aux / 2 != 0:
        output = [aux % 2] + output
        aux //= 2

    return output
