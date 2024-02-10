# 120. Triangle
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        a = triangle[:]

        for i in range(1, n):
            for j in range(i + 1):
                a[i][j] += min(
                    a[i - 1][j] if j < i else float("inf"),
                    a[i - 1][j - 1] if j > 0 else float("inf"),
                )

        return min(a[-1])
