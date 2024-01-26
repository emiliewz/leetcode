# 802. Find Eventual Safe States
from collections import defaultdict, deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        safe = []
        for i, j in enumerate(graph):
            if j:
                for k in j:
                    g[k].add(i)
            else:
                safe.append(i)

        q = deque(safe)
        while q:
            cur = q.popleft()
            for node in g[cur]:
                graph[node].remove(cur)
                if not graph[node]:
                    q.append(node)
                    safe.append(node)

        safe.sort()
        return safe


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        to = {i: set() for i in range(n)}
        g = defaultdict(set)
        q = deque()
        safe = []

        for i, j in enumerate(graph):
            if not j:
                q.append(i)
            else:
                to[i].update(j)
                for k in j:
                    g[k].add(i)
        while q:
            cur = q.popleft()
            safe.append(cur)
            for node in g[cur]:
                to[node].remove(cur)
                if not to[node]:
                    q.append(node)
            to.pop(cur)

        safe.sort()
        return safe
