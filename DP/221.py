# 221. Maximal Square
from math import isqrt
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        a = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    a[i][j] = min(a[i - 1][j], a[i - 1][j - 1], a[i][j - 1]) + 1
                    res = max(res, a[i][j])
        return res**2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        a = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    a[i][j] = (
                        min(a[i - 1][j][0], a[i - 1][j - 1][0]) + 1,
                        min(a[i][j - 1][1], a[i - 1][j - 1][1]) + 1,
                    )
                    max_len = max(max_len, min(a[i][j]))
        return max_len**2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(dp[i][j], res)
        return res**2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = (
                        min(
                            dp[i - 1][j - 1] if i > 0 and j > 0 else 0,
                            dp[i - 1][j] if i > 0 else 0,
                            dp[i][j - 1] if j > 0 else 0,
                        )
                        + 1
                    )
                res = max(dp[i][j], res)
        return res**2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        squares = [[0] * (n) for _ in range(m)]
        max_square = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    squares[i][j] = int(matrix[i][j])
                elif (
                    not int(matrix[i - 1][j - 1])
                    or not int(matrix[i - 1][j])
                    or not int(matrix[i][j - 1])
                    or not int(matrix[i][j])
                ):
                    squares[i][j] = int(matrix[i][j])
                else:
                    squares[i][j] = (
                        isqrt(
                            min(
                                int(squares[i - 1][j - 1]),
                                int(squares[i - 1][j]),
                                int(squares[i][j - 1]),
                            )
                        )
                        + 1
                    ) ** 2
                max_square = max(squares[i][j], max_square)
        return max_square
