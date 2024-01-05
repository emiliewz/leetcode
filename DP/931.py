# 931. Minimum Falling Path Sum
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        fall_sum = [[200] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    fall_sum[i][j] = matrix[i][j]
                elif j == 0:
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
