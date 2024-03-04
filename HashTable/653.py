# 653. Two Sum IV - Input is a BST
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a = set()
        q = deque([root])
        while q:
            cur = q.popleft()
            diff = k - cur.val
            if diff in a:
                return True
            a.add(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return False
