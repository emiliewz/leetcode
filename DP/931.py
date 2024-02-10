# 931. Minimum Falling Path Sum
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        a = [[float("inf")] + i + [float("inf")] for i in matrix]

        for i in range(1, n):
            for j in range(1, n + 1):
                a[i][j] += min(a[i - 1][j], a[i - 1][j - 1], a[i - 1][j + 1])

        return min(a[-1])
