from __future__ import annotations


class ListNode:
    def append(self, node: ListNode):
        if self.next is None:
            self.next = node
        else:
            self.next.append(node)

    def __init__(self, val: int = 0, next: ListNode = None):
        self.value = val
        self.next = next