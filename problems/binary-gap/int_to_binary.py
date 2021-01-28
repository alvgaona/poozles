def int_to_binary(n):
    if n == 0:
        return [0]

    output = []

    aux = n
    while aux / 2 != 0:
        output = [aux % 2] + output
        aux //= 2

    return output
