# 687. Longest Univalue Path
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, tar):
            if not cur:
                return 0
            nonlocal max_len
            left = dfs(cur.left, cur.val)
            right = dfs(cur.right, cur.val)
            max_len = max(max_len, left + right)
            if cur.val == tar:
                return max(left, right) + 1
            return 0

        if not root:
            return 0
        max_len = 0
        dfs(root, root.val)
        return max_len
