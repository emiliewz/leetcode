# 501. Find Mode in Binary Search Tree
from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        a = defaultdict(int)
        q = deque([root])
        while q:
            cur = q.popleft()
            a[cur.val] += 1
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        mc = max(a.values())
        return [i for i in a if a[i] == mc]
