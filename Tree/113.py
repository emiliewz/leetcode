# 113. Path Sum II
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root):
            cur.append(root.val)

            if not root.left and not root.right and sum(cur) == targetSum:
                res.append(cur[:])
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            cur.pop()

        if not root:
            return None
        res, cur = [], []
        dfs(root)
        return res
