# 980. Unique Paths III
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        zeros, res = 1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    zeros += 1

        def dfs(i, j, k):
            nonlocal res
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return

            if grid[i][j] == 2:
                res += k == 0
                return
            grid[i][j] = -1
            for dx, dy in [(0, 1), (1, 0)]:
                dfs(i + dx, j + dy, k - 1)
                dfs(i - dx, j - dy, k - 1)
            grid[i][j] = 0

        dfs(sx, sy, zeros)
        return res
