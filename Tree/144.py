# 144. Binary Tree Preorder Traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack, res = root, [], []

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            cur = cur.right

        return res
