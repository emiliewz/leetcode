# 99. Recover Binary Search Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, stack, res, prev = root, [], [], TreeNode(-float("inf"))
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val < prev.val:
                res.append((prev, cur))
            prev = cur
            cur = cur.right

        res[0][0].val, res[-1][1].val = res[-1][1].val, res[0][0].val

        return root
