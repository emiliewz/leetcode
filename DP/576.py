# 576. Out of Boundary Paths
from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        MOD = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        @cache
        def dp(x, y, k):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if k == 0:
                return 0

            res = 0
            for dx, dy in directions:
                res += dp(x + dx, y + dy, k - 1)
            return res % MOD

        return dp(startRow, startColumn, maxMove)


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        memo = {}

        def dfs(x, y, move):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1

            if move == maxMove:
                return 0

            if (x, y, move) in memo:
                return memo[(x, y, move)]

            res = 0
            for dx, dy in directions:
                res += dfs(x + dx, y + dy, move + 1)

            memo[(x, y, move)] = res
            return res

        return dfs(startRow, startColumn, 0) % (10**9 + 7)
