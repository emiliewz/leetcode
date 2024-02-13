# 145. Binary Tree Postorder Traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, res = [root], []

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return res[::-1]
