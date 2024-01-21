# 675. Cut Off Trees for Golf Event
from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = []

        for i in range(m):
            for j in range(n):
                cur = forest[i][j]
                if cur > 1:
                    trees.append([cur, i, j])
        trees.sort()

        def bfs(sx, sy, tx, ty):
            q = deque()
            q.append((sx, sy))
            steps = 0
            visit = set()

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if x == tx and y == ty:
                        return steps
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx = x + dx
                        ny = y + dy
                        if (
                            0 <= nx < m
                            and 0 <= ny < n
                            and forest[nx][ny]
                            and (nx, ny) not in visit
                        ):
                            visit.add((x + dx, y + dy))
                            q.append((x + dx, y + dy))

                steps += 1
            return -1

        res = 0
        sx, sy = 0, 0
        for tree in trees:
            steps = bfs(sx, sy, tree[1], tree[2])
            if steps < 0:
                return -1
            res += steps
            sx, sy = tree[1], tree[2]

        return res


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        r = len(forest)
        c = len(forest[0])
        trees = []

        for i in range(r):
            for j in range(c):
                if forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])
        trees.sort()

        def bfs(sx, sy, tx, ty):
            visit = set()
            q = deque()
            q.append((sx, sy))
            res = 0
            while q:
                for _ in range(len(q)):
                    cx, cy = q.popleft()
                    if cx == tx and cy == ty:
                        return res
                    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = cx + i, cy + j
                        if (
                            0 <= nx < r
                            and 0 <= ny < c
                            and forest[nx][ny]
                            and (nx, ny) not in visit
                        ):
                            visit.add((nx, ny))
                            q.append((nx, ny))
                res += 1
            return -1

        start_x = 0
        start_y = 0
        res = 0
        for t in trees:
            move = bfs(start_x, start_y, t[1], t[2])
            if move == -1:
                return -1
            res += move
            start_x = t[1]
            start_y = t[2]
        return res
