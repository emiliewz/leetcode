# 63. Unique Paths II
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        a = [[0] * (n + 1) for _ in range(m + 1)]
        a[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    a[i][j] = a[i - 1][j] + a[i][j - 1]

        return a[-1][-1]
