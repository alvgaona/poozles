# https://leetcode.com/problems/merge-k-sorted-lists

from list_node import ListNode


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    output_node = ListNode(None, None)
    heads = {}
    min_node = [0, lists[0]]
    
    for i in range(0, len(lists)):
        heads[i] = lists[i]

    while list(heads.values()) != [None]*len(list(heads.values())):
        heads_values = list(heads.values())
        for i, node in enumerate(heads_values):
            if node is not None:
                if node.value < min_node[1].value:
                    min_node[0] = i
                    min_node[1] = node
        heads[min_node[0]] = heads[min_node[0]].next
        min_node[1].next = None
        output_node.append(min_node[1])
        aux = list(heads.values())
        for i, v in enumerate(aux):
            if v is not None:
                min_node[0] = i
                min_node[1] = v
                break
                
    return output_node.next
