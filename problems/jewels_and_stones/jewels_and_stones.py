# https://leetcode.com/problems/jewels-and-stones

def jewels_and_stones(jewels: str, stones: str) -> int:
    jewels_set = set([jewel for jewel in jewels])

    stone_jewel_counter = 0
    for stone in stones:
        if stone in jewels_set:
            stone_jewel_counter += 1

    return stone_jewel_counter

