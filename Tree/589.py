# 589. N-ary Tree Preorder Traversal
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        stack, res = [root], []

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(reversed(cur.children))

        return res
