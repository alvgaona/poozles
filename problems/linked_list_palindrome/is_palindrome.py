# https://leetcode.com/problems/palindrome-linked-list

from list_node import ListNode


def is_palindrome(head: ListNode):
    if head is None:
        return True

    slow, fast = head, head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    if fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Reverse second part
    before = slow
    slow = slow.next
    before.next = None

    while slow is not None:
        after = slow.next
        slow.next = before
        before = slow
        slow = after

    while fast is not None and head is not None:
        if fast.val != head.val:
            return False

        fast = fast.next
        head = head.next

    return True
