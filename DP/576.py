# 576. Out of Boundary Paths
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
