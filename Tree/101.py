# 101. Symmetric Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, root)])

        while q:
            i, j = q.popleft()
            if i.val != j.val:
                return False

            if i.left or j.right:
                if i.left and j.right:
                    q.append((i.left, j.right))
                else:
                    return False

            if i.right or j.left:
                if i.right and j.left:
                    q.append((i.right, j.left))
                else:
                    return False

        return True
