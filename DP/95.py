# 95. Unique Binary Search Trees II
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_tree = generate_trees(start, i - 1)
                right_tree = generate_trees(i + 1, end)
                for l in left_tree:
                    for r in right_tree:
                        node = TreeNode(i, l, r)
                        all_trees.append(node)
            return all_trees

        return generate_trees(1, n)
