# 1162. As Far from Land as Possible
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = 0
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    grid[i][j] = 1
                    zeros += 1
                else:
                    grid[i][j] = 0

        if not zeros or zeros == n**2:
            return -1

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    top = grid[i - 1][j] if i > 0 else float("inf")
                    left = grid[i][j - 1] if j > 0 else float("inf")
                    grid[i][j] = min(top, left) + 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    down = grid[i + 1][j] if i + 1 < n else float("inf")
                    right = grid[i][j + 1] if j + 1 < n else float("inf")
                    grid[i][j] = min(grid[i][j], min(down, right) + 1)

        res = max(max(grid[i]) for i in range(n))
        return res
