# 688. Knight Probability in Chessboard
from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        direct = [(1, 2), (1, -2), (-2, 1), (2, 1)]

        @cache
        def dfs(i, j, k):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            if k == 0:
                return 1

            res = 0
            for dx, dy in direct:
                res += dfs(i + dx, j + dy, k - 1) / 8 + dfs(i - dx, j - dy, k - 1) / 8

            return res

        return dfs(row, column, k)
