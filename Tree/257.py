# 257. Binary Tree Paths
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, cur):
            if not root.left and not root.right:
                res.append("->".join(cur))
                return
            if root.left:
                dfs(root.left, cur + [str(root.left.val)])
            if root.right:
                dfs(root.right, cur + [str(root.right.val)])

        res = []
        dfs(root, [str(root.val)])
        return res
