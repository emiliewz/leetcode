# 965. Univalued Binary Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v = root.val
        q = deque([root])
        while q:
            cur = q.popleft()

            if cur.left:
                if cur.left.val == v:
                    q.append(cur.left)
                else:
                    return False
            if cur.right:
                if cur.right.val == v:
                    q.append(cur.right)
                else:
                    return False

        return True
