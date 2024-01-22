# 133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        q = deque([node])
        a = {node.val: Node(node.val)}

        while q:
            cur = q.popleft()
            copy = a[cur.val]

            for nei in cur.neighbors:
                if nei.val not in a:
                    a[nei.val] = Node(nei.val)
                    q.append(nei)

                copy.neighbors.append(a[nei.val])

        return a[node.val]


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        a = {}

        def dfs(node):
            if node.val in a:
                return a[node.val]

            copy = Node(node.val)
            a[node.val] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        a = {}

        def dfs(node):
            if node in a:
                return a[node]
            copy = Node(node.val)
            a[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
