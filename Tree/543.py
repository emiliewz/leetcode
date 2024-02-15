# 543. Diameter of Binary Tree
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0

        def dfs(cur):
            nonlocal max_len
            if not cur:
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            max_len = max(left + right, max_len)
            return max(left, right) + 1

        dfs(root)
        return max_len
