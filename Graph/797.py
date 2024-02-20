# 797. All Paths From Source to Target
from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q, n = deque([(0, [0])]), len(graph)
        res = []

        while q:
            i, cur = q.popleft()
            if i == n - 1:
                res.append(cur)
            else:
                for nei in graph[i]:
                    q.append((nei, cur + [nei]))

        return res
