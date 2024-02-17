# 98. Validate Binary Search Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, l, h):
            if not root:
                return True
            if root.val >= h or root.val <= l:
                return False
            return check(root.left, l, root.val) and check(root.right, root.val, h)

        return check(root, -float("inf"), float("inf"))
