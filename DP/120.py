# 120. Triangle
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        fall_sum = matrix[:]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    fall_sum[i][j] = (
                        min(fall_sum[i - 1][j], fall_sum[i - 1][j + 1]) + matrix[i][j]
                    )
                elif j == n - 1:
                    fall_sum[i][j] = (
                        min(fall_sum[i - 1][j - 1], fall_sum[i - 1][j]) + matrix[i][j]
                    )
                else:
                    fall_sum[i][j] = (
                        min(
                            fall_sum[i - 1][j - 1],
                            fall_sum[i - 1][j],
                            fall_sum[i - 1][j + 1],
                        )
                        + matrix[i][j]
                    )

        return min(fall_sum[-1])


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
