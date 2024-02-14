# 987. Vertical Order Traversal of a Binary Tree
from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0, 0)])
        a = defaultdict(list)

        while q:
            cur, i, j = q.popleft()
            a[j].append((i, cur.val))
            if cur.left:
                q.append((cur.left, i + 1, j - 1))
            if cur.right:
                q.append((cur.right, i + 1, j + 1))

        return [[v for (i, v) in sorted(item)] for (y, item) in sorted(a.items())]
