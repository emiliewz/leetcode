# 429. N-ary Tree Level Order Traversal
from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        q, res = deque([root]), []
        if not root:
            return []
        while q:
            cur_list = []
            for _ in range(len(q)):
                cur = q.popleft()
                cur_list.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        q.append(child)
            res.append(cur_list)

        return res
