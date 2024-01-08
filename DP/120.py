# 120. Triangle
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        min_path = triangle[:]
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    min_path[i][j] += min_path[i - 1][j]
                elif j == i:
                    min_path[i][j] += min_path[i - 1][j - 1]
                else:
                    min_path[i][j] += min(min_path[i - 1][j], min_path[i - 1][j - 1])
        return min(min_path[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        steps = [[0] * (i + 1) for i in range(n)]
        steps[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    steps[i][j] = triangle[i][j] + steps[i - 1][j]
                elif j == i:
                    steps[i][j] = triangle[i][j] + steps[i - 1][j - 1]
                else:
                    steps[i][j] = triangle[i][j] + min(
                        steps[i - 1][j - 1], steps[i - 1][j]
                    )
        return min(steps[-1])
