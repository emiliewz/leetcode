# 1210. Minimum Moves to Reach Target with Rotations
from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
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
                    if i + 1 < n and not grid[i + 1][j + 1] and not grid[i + 1][j]:
                        q.append((i, j, "v"))
                        q.append((i + 1, j, "h"))
                    if j + 2 < n and not grid[i][j + 2]:
                        q.append((i, j + 1, "h"))
                else:
                    if j + 1 < n and not grid[i][j + 1] and not grid[i + 1][j + 1]:
                        q.append((i, j, "h"))
                        q.append((i, j + 1, "v"))
                    if i + 2 < n and not grid[i + 2][j]:
                        q.append((i + 1, j, "v"))

            moves += 1
        return -1
