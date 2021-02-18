# https://leetcode.com/problems/top-k-frequent-words

import heapq


def top_k_sorting(words: list[str], k: int) -> list[str]:
    """
    Time complexity: O(nlog(n))
    Space complexity: O(n)
    """
    count = {}

    for word in words:
        if count.get(word) is not None:
            count[word] += 1
        else:
            count[word] = 1

    items = list(count.items())
    items.sort(key=lambda x: (-x[1], x[0]))

    return [items[i][0] for i in range(0, k)]


def top_k_heap(words: list[str], k: int) -> list[str]:
    """
    Time complexity: O(nlog(k))
    Space complexity: O(n)
    """
    count = {}

    for word in words:
        if count.get(word) is not None:
            count[word] += 1
        else:
            count[word] = 1

    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
