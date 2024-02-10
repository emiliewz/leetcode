# 221. Maximal Square
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
