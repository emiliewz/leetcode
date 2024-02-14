# 437. Path Sum III
from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, total):
            nonlocal res
            if not root:
                return

            total += root.val
            prev_sum = total - targetSum

            res += a[prev_sum]
            a[total] += 1

            dfs(root.left, total)
            dfs(root.right, total)

            a[total] -= 1

        if not root:
            return 0
        a = defaultdict(int)
        a[0] = 1
        res = 0
        dfs(root, 0)
        return res
