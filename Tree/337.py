# 337. House Robber III
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def rob(node):
            if not node:
                return (0, 0)

            left = rob(node.left)
            right = rob(node.right)

            cur = node.val + left[1] + right[1]
            later = max(left) + max(right)

            return (cur, later)

        return max(rob(root))
