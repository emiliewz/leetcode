# 100. Same Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return not p and not q

        dq = deque([(p, q)])

        while dq:
            i, j = dq.popleft()

            if i.val != j.val:
                return False

            if i.left or j.left:
                if i.left and j.left:
                    dq.append((i.left, j.left))
                else:
                    return False

            if i.right or j.right:
                if i.right and j.right:
                    dq.append((i.right, j.right))
                else:
                    return False

        return True
