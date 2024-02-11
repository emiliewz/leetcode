# 576. Out of Boundary Paths
from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if k == 0:
                return 0

            res = 0
            for dx, dy in direct:
                res += dfs(i + dx, j + dy, k - 1)
            return res

        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)
