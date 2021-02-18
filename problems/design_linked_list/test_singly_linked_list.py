import unittest

from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def test_singly_linked_list(self):
        linked_list = SinglyLinkedList()
    
        result = [
            linked_list.prepend(7),
            linked_list.prepend(2),
            linked_list.prepend(1),
            linked_list.add(3, 0),
            linked_list.remove(2),
            linked_list.prepend(6),
            linked_list.append(4),
            linked_list.get(4),
            linked_list.prepend(4),
            linked_list.add(5, 0),
            linked_list.prepend(6)
        ]
    
        self.assertListEqual(result, [None, None, None, None, None, None, None, 4, None, None, None])
