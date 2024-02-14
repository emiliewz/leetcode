# 112. Path Sum
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], hasPathSum: int) -> bool:
        if not root:
            return False

        cur = hasPathSum - root.val
        if not root.left and not root.right:
            return not cur

        return self.hasPathSum(root.left, cur) or self.hasPathSum(root.right, cur)
