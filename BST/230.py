# 230. Kth Smallest Element in a BST
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur, stack, count = root, [], 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if count == k - 1:
                return cur.val
            else:
                count += 1
            cur = cur.right
        return cur.val
