# 968. Binary Tree Cameras
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(cur):
            nonlocal res
            if not cur:
                return 2
            left = dfs(cur.left)
            right = dfs(cur.right)

            if left == 0 or right == 0:
                res += 1
                return 1

            return 2 if left == 1 or right == 1 else 0

        return (dfs(root) == 0) + res
