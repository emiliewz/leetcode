# 1039. Minimum Score Triangulation of Polygon
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        a = [[float("inf")] * n for _ in range(n)]
        for i in range(n - 1):
            a[i][i + 1] = 0

        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i + 1, j):
                    a[i][j] = min(
                        a[i][j], values[i] * values[j] * values[k] + a[i][k] + a[k][j]
                    )

        return a[0][n - 1]
