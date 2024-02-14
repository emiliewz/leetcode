# 104. Maximum Depth of Binary Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        max_depth = 0

        while q:
            cur, x = q.popleft()
            if x > max_depth:
                max_depth = x

            if cur.left:
                q.append((cur.left, x + 1))
            if cur.right:
                q.append((cur.right, x + 1))

        return max_depth + 1
