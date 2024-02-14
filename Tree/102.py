# 102. Binary Tree Level Order Traversal
from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q, res = deque([root]), []

        while q:
            cur_list = []
            for _ in range(len(q)):
                cur = q.popleft()
                cur_list.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(cur_list)

        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        a = defaultdict(list)

        while q:
            cur, x = q.popleft()
            a[x].append(cur.val)
            if cur.left:
                q.append((cur.left, x + 1))
            if cur.right:
                q.append((cur.right, x + 1))

        return [j for _, j in sorted(a.items())]
