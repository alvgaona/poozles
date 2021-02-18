# https://leetcode.com/problems/find-largest-value-in-each-tree-row

from tree_node import TreeNode


def largest_value_row(root: TreeNode) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def helper(node, depth, res):
        if not node:
            return
        if depth == len(res):
            res.append(node.val)
        else:
            res[depth] = max(res[depth], node.val)

        helper(node.left, depth + 1, res)
        helper(node.right, depth + 1, res)

    result = []
    helper(root, 0, result)
    return result
