# 129. Sum Root to Leaf Numbers
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root, total):
            cur = root.val
            if not root.left and not root.right:
                res.append(total * 10 + cur)

            if root.left:
                dfs(root.left, total * 10 + cur)

            if root.right:
                dfs(root.right, total * 10 + cur)

        dfs(root, 0)
        return sum(res)
