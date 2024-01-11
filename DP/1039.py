# 1039. Minimum Score Triangulation of Polygon
from functools import cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
            res = float("inf")
            for k in range(i + 1, j):
                res = min(res, values[k] * values[i] * values[j] + dp(i, k) + dp(k, j))
            return res if res != float("inf") else 0

        return dp(0, len(values) - 1)


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
            if i + 1 == j:
                return 0
            res = float("inf")
            for k in range(i + 1, j):
                res = min(res, values[k] * values[i] * values[j] + dp(i, k) + dp(k, j))
            return res

        return dp(0, len(values) - 1)
