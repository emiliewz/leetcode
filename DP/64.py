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


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_sum = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        min_sum[0][1] = min_sum[1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                min_sum[i][j] = (
                    min(min_sum[i - 1][j], min_sum[i][j - 1]) + grid[i - 1][j - 1]
                )

        return min_sum[-1][-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        steps = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    steps[i][j] = grid[i][j]
                elif i == 0:
                    steps[i][j] = grid[i][j] + steps[i][j - 1]
                elif j == 0:
                    steps[i][j] = grid[i][j] + steps[i - 1][j]
                else:
                    steps[i][j] = grid[i][j] + min(steps[i - 1][j], steps[i][j - 1])
        return steps[-1][-1]
