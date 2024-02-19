# 530. Minimum Absolute Difference in BST
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, l, h):
            if not cur:
                return h - l
            left = dfs(cur.left, l, cur.val)
            right = dfs(cur.right, cur.val, h)
            return min(left, right)

        return dfs(root, -float("inf"), float("inf"))
