# 590. N-ary Tree Postorder Traversal
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        stack, res = [root], []

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)

        return res[::-1]
