# 872. Leaf-Similar Trees
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf = []
        stack = [root1]

        while stack:
            cur = stack.pop()
            if cur.left or cur.right:
                if cur.left:
                    stack.append((cur.left))
                if cur.right:
                    stack.append((cur.right))
            else:
                leaf.append(cur.val)
        stack.append(root2)

        while stack:
            cur = stack.pop()
            if cur.left or cur.right:
                if cur.left:
                    stack.append((cur.left))
                if cur.right:
                    stack.append((cur.right))
            else:
                if not leaf or cur.val != leaf.pop(0):
                    return False

        return not leaf
