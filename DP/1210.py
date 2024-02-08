# 1210. Minimum Moves to Reach Target with Rotations
from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = 0
        q = deque([(0, 0, "h")])
        visit = set()

        while q:
            for _ in range(len(q)):
                i, j, diret = q.popleft()

                if (i, j, diret) in visit:
                    continue

                visit.add((i, j, diret))

                if (i, j) == (n - 1, n - 2):
                    return moves

                if diret == "h":
                    if i + 1 < m and not grid[i + 1][j + 1] and not grid[i + 1][j]:
                        q.append((i, j, "v"))
                        q.append((i + 1, j, "h"))
                    if j + 2 < n and not grid[i][j + 2]:
                        q.append((i, j + 1, "h"))
                else:
                    if j + 1 < n and not grid[i][j + 1] and not grid[i + 1][j + 1]:
                        q.append((i, j, "h"))
                        q.append((i, j + 1, "v"))
                    if i + 2 < m and not grid[i + 2][j]:
                        q.append((i + 1, j, "v"))

            moves += 1
        return -1


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        q.append((0, 0, "h"))
        visit = set()
        res = 0

        while q:
            for _ in range(len(q)):
                x, y, d = q.popleft()
                if x < 0 or x >= n or y < 0 or y >= n or (x, y, d) in visit:
                    continue
                visit.add((x, y, d))
                if (x, y, d) == (n - 1, n - 2, "h"):
                    return res
                if d == "h":
                    if (
                        x + 1 < n
                        and y + 1 < n
                        and grid[x + 1][y] == 0
                        and grid[x + 1][y + 1] == 0
                    ):
                        q.append((x, y, "v"))
                        q.append((x + 1, y, "h"))
                    if y + 2 < n and grid[x][y + 2] == 0:
                        q.append((x, y + 1, "h"))
                else:
                    if (
                        y + 1 < n
                        and x + 1 < n
                        and grid[x][y + 1] == 0
                        and grid[x + 1][y + 1] == 0
                    ):
                        q.append((x, y + 1, "v"))
                        q.append((x, y, "h"))
                    if x + 2 < n and grid[x + 2][y] == 0:
                        q.append((x + 1, y, "v"))
            res += 1
        return -1


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        q.append((0, 0, "h"))
        res = 0
        visit = set()
        while q:
            for _ in range(len(q)):
                x, y, d = q.popleft()
                if (x, y, d) == (n - 1, n - 2, "h"):
                    return res
                if (x, y, d) in visit:
                    continue
                visit.add((x, y, d))
                if d == "h":
                    if y + 2 < n and not grid[x][y + 2]:
                        q.append((x, y + 1, d))
                    if x + 1 < n and not grid[x + 1][y] and not grid[x + 1][y + 1]:
                        q.append((x + 1, y, d))
                        q.append((x, y, "v"))
                else:
                    if x + 2 < n and not grid[x + 2][y]:
                        q.append((x + 1, y, d))
                    if y + 1 < n and not grid[x][y + 1] and not grid[x + 1][y + 1]:
                        q.append((x, y + 1, d))
                        q.append((x, y, "h"))
            res += 1
        return -1
