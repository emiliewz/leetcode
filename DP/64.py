# 64. Minimum Path Sum
from typing import List


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
