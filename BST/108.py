# 108. Convert Sorted Array to Binary Search Tree
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, h):
            if l > h:
                return None
            mid = l + (h - l) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, h)
            return node

        return dfs(0, len(nums) - 1)
