# 785. Is Graph Bipartite?
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if graph == [[]]:
            return True
        n = len(graph)
        color = {}
        for idx in range(n):
            if idx not in color:
                color[idx] = 0
                q = deque([(idx, 0)])

                while q:
                    i, c = q.popleft()
                    for nei in graph[i]:
                        nei_c = c ^ 1
                        if nei in color:
                            if color[nei] != nei_c:
                                return False
                        else:
                            color[nei] = nei_c
                            q.append((nei, nei_c))
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}

        for i in range(n):
            if i not in color:
                color[i] = 0
            q = deque([i])

            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei in color and color[nei] == color[cur]:
                        return False
                    if nei not in color:
                        q.append(nei)
                        color[nei] = color[cur] ^ 1

        return True
