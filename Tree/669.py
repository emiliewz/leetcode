# 669. Trim a Binary Search Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high) if root.val > low else None
        root.right = self.trimBST(root.right, low, high) if root.val < high else None

        return root
