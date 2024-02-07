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


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        steps = [[0] * (n + 1) for _ in range(m + 1)]
        steps[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    steps[i][j] = steps[i - 1][j] + steps[i][j - 1]

        return steps[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        steps = [[1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    steps[i][j] = 0
                elif i == 0 and j > 0 and steps[i][j - 1] == 0:
                    steps[i][j] = 0
                elif j == 0 and i > 0 and steps[i - 1][j] == 0:
                    steps[i][j] = 0
                elif i > 0 and j > 0:
                    steps[i][j] = steps[i - 1][j] + steps[i][j - 1]

        print(steps)
        return steps[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        steps = [[0] * (n + 1) for _ in range(m + 1)]
        steps[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    steps[i][j] = steps[i - 1][j] + steps[i][j - 1]
        return steps[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        steps = [[0] * (n + 1) for _ in range(m + 1)]
        steps[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not obstacleGrid[i][j]:
                    steps[i][j] = steps[i + 1][j] + steps[i][j + 1]

        return steps[0][0]
