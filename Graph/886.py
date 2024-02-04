# 886. Possible Bipartition
from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = {}

        for i in range(n):
            if i not in color:
                color[i] = 0
                q = deque([i])
                while q:
                    cur = q.popleft()
                    cur_color = color[cur]

                    for nei in graph[cur]:
                        if nei in color:
                            if color[nei] == cur_color:
                                return False
                        else:
                            color[nei] = cur_color ^ 1
                            q.append(nei)

        return True


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)
        color = {}

        for i in range(1, n + 1):
            if i not in color:
                color[i] = 0
                q = deque([i])
                while q:
                    cur = q.popleft()
                    for d in graph[cur]:
                        if d in color and color[d] == color[cur]:
                            return False
                        if d not in color:
                            q.append(d)
                            color[d] = color[cur] ^ 1

        return True
