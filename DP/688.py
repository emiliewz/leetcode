# 688. Knight Probability in Chessboard
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (-1, -2),
            (-1, 2),
            (-2, -1),
            (-2, 1),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
        ]
        memo = {}

        def dfs(i, j, move):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0

            if move == k:
                return 1

            if (i, j, move) in memo:
                return memo[(i, j, move)]

            res = 0
            for dx, dy in directions:
                res += dfs(i + dx, j + dy, move + 1) / 8

            memo[(i, j, move)] = res
            return res

        return dfs(row, column, 0)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        res = 0
        directions = [(-1, -2), (-1, 2), (-2, -1), (-2, 1)]

        def dfs(i, j, move, p):
            if i < 0 or i >= n or j < 0 or j >= n:
                return

            if move == k:
                nonlocal res
                res += p
                return

            for dx, dy in directions:
                dfs(i + dx, j + dy, move + 1, p / 8)
                dfs(i - dx, j - dy, move + 1, p / 8)

        dfs(row, column, 0, 1)
        return res