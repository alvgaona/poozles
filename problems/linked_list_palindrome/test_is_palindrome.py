import unittest

from list_node import ListNode
from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))

        self.assertTrue(is_palindrome(head))
