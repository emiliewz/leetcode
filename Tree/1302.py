# 1302. Deepest Leaves Sum
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        res, max_depth = 0, 0

        while q:
            cur, x = q.popleft()
            if x > max_depth:
                max_depth = x
                res = 0
            res += cur.val

            if cur.left:
                q.append((cur.left, x + 1))
            if cur.right:
                q.append((cur.right, x + 1))

        return res
