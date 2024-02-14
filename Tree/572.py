# 572. Subtree of Another Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubtree(root):
            q = deque([(root, subRoot)])
            while q:
                i, j = q.popleft()
                if i.val != j.val:
                    return False
                if i.left or j.left:
                    if i.left and j.left:
                        q.append((i.left, j.left))
                    else:
                        return False
                if i.right or j.right:
                    if i.right and j.right:
                        q.append((i.right, j.right))
                    else:
                        return False
            return True

        if not subRoot:
            return False
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.val == subRoot.val:
                if isSubtree(cur):
                    return True
            if cur.left:
                q.append((cur.left))
            if cur.right:
                q.append((cur.right))

        return False
