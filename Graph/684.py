# 684. Redundant Connection
from collections import defaultdict, deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(set)

        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        ends = [i for i in graph if len(graph[i]) == 1]

        q = deque(ends)
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                for nei in graph[i]:
                    graph[nei].remove(i)
                    if len(graph[nei]) == 1:
                        q.append(nei)
                graph.pop(i)
        for i, j in edges[::-1]:
            if i in graph and j in graph[i]:
                return (i, j)

        return []
