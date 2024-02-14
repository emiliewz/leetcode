# 814. Binary Tree Pruning
from collections import deque
from functools import cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        @cache
        def canPrun(root):
            if not root:
                return True
            return not root.val and canPrun(root.left) and canPrun(root.right)

        q = deque([root])

        while q:
            cur = q.popleft()

            if cur and canPrun(cur.left):
                cur.left = None
            else:
                q.append(cur.left)

            if cur and canPrun(cur.right):
                cur.right = None
            else:
                q.append(cur.right)

        if not root.val and not root.left and not root.right:
            return None

        return root
