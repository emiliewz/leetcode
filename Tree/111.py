# 111. Minimum Depth of Binary Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        k = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return k

                if cur.left:
                    q.append((cur.left))
                if cur.right:
                    q.append((cur.right))
            k += 1

        return k
