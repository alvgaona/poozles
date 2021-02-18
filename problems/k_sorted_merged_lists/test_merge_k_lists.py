import unittest

from merge_k_lists import merge_k_lists
from list_node import ListNode


class TestMergeKLists(unittest.TestCase):
    def test_merge_k_lists(self):
        l02 = ListNode(5, None)
        l01 = ListNode(4, l02)
        l00 = ListNode(1, l01)
    
        l12 = ListNode(4, None)
        l11 = ListNode(3, l12)
        l10 = ListNode(1, l11)
    
        l21 = ListNode(6, None)
        l20 = ListNode(2, l21)
    
        input = [l00, l10, l20]
    
        output = merge_k_lists(input)
        
        itr = output
        while itr is not None:
            print(itr.value)
            itr = itr.next