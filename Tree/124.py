# 124. Binary Tree Maximum Path Sum
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")

        def dfs(cur):
            nonlocal max_sum
            if not cur:
                return 0
            left = max(dfs(cur.left), 0)
            right = max(dfs(cur.right), 0)
            max_sum = max(cur.val + left + right, max_sum)

            return cur.val + max(left, right)

        dfs(root)
        return max_sum
