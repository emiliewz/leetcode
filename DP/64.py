# 64. Minimum Path Sum
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        a = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        a[0][1] = a[1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a[i][j] = min(a[i][j - 1], a[i - 1][j]) + grid[i - 1][j - 1]

        return a[-1][-1]
