# 417. Pacific Atlantic Water Flow
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        alt = set([(i, n - 1) for i in range(m)])
        alt.update([(m - 1, j) for j in range(n)])
        pac = set([(i, 0) for i in range(m)])
        pac.update([(0, j) for j in range(n)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(isAlt):
            q = deque(alt) if isAlt else deque(pac)
            visit = alt if isAlt else pac
            while q:
                cx, cy = q.popleft()
                for dx, dy in directions:
                    i, j = cx + dx, cy + dy
                    if (
                        (i, j) not in visit
                        and 0 <= i < m
                        and 0 <= j < n
                        and heights[i][j] >= heights[cx][cy]
                    ):
                        q.append((i, j))
                        visit.add((i, j))
            return visit

        alt = bfs(True)
        pac = bfs(False)

        return list(alt & pac)
