# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        a, b = min(p.val, q.val), max(p.val, q.val)
        cur = root

        while cur:
            if cur.val > b:
                cur = cur.left
            elif cur.val < a:
                cur = cur.right
            else:
                return cur

        return None
