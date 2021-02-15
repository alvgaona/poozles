import unittest

from tree_node import TreeNode
from largest_value_row import largest_value_row


class TestLargestValueInTreeRow(unittest.TestCase):
    def test_01(self):
        root = TreeNode(1, TreeNode(3, TreeNode(5, None, None), TreeNode(3, None, None)), TreeNode(2, None, TreeNode(9, None, None)))
        self.assertEqual(largest_value_row(root), [1, 3, 9])

    def test_02(self):
        root = TreeNode(5, TreeNode(14, TreeNode(1, None, None), None), None)
        self.assertEqual(largest_value_row(root), [5, 14, 1])

    def test_03(self):
        root = TreeNode(3, None, TreeNode(30, TreeNode(10, None, TreeNode(15, None, TreeNode(45, None, None))), None))
        self.assertEqual(largest_value_row(root), [3, 30, 10, 15, 45])
