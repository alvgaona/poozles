#!/usr/bin/python3
from collections.abc import Generator


def compress(strand: str) -> str:
    result = []
    counter = 1
    current = strand[0]

    for i in range(1, len(strand) + 1):
        if i < len(strand):
            if strand[i] == current:
                counter += 1
                continue

        if counter == 1:
            result.append(current)
        else:
            result.append(str(counter))
            result.append(current)
            counter = 1

        if i < len(strand):
            current = strand[i]

    return ''.join(result)


def compress_prima(strand: str) -> str:
    result = []
    counter = 1

    for i in range(0, len(strand)):
        current = strand[i]
        if i < len(strand) - 1:
            j = i + 1

            if current == strand[j]:
                counter += 1
                continue

        if counter == 1:
            result.append(current)
        else:
            result.append(str(counter))
            result.append(current)
            counter = 1

    return ''.join(result)


def compress_generator(strand: str) -> Generator[str]:
    counter = 1

    for i in range(0, len(strand)):
        current = strand[i]
        if i < len(strand) - 1:
            j = i + 1

            if current == strand[j]:
                counter += 1
                continue

        if counter == 1:
            yield current
        else:
            yield str(counter) + current
            counter = 1


def main():
    strand = 'AAACTTTTTAGCCCCCCCGGGGTTTTTAAA'

    assert compress(strand) == '3AC5TAG7C4G5T3A'
    assert compress_prima(strand) == '3AC5TAG7C4G5T3A'
    assert ''.join(compress_generator(strand)) == '3AC5TAG7C4G5T3A'


if __name__ == '__main__':
    exit(main())
