# 675. Cut Off Trees for Golf Event
from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sx, sy, tx, ty):
            q = deque([(sx, sy)])
            visit, steps = set(), 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if (x, y) == (tx, ty):
                        return steps
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        i, j = x + dx, y + dy
                        if (
                            (i, j) not in visit
                            and 0 <= i < m
                            and 0 <= j < n
                            and forest[i][j]
                        ):
                            visit.add((i, j))
                            q.append((i, j))

                steps += 1
            return -1

        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        start, res = (0, 0), 0
        trees.sort()

        for _, i, j in trees:
            steps = bfs(*start, i, j)
            if steps == -1:
                return -1
            res += steps
            start = (i, j)

        return res
