# 304. Range Sum Query 2D - Immutable
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sums[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.sums[i][j - 1]
                    + self.sums[i - 1][j]
                    - self.sums[i - 1][j - 1]
                )
        print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == col1 == 0:
            return self.sums[row2 + 1][col2 + 1]
        return (
            self.sums[row2 + 1][col2 + 1]
            - self.sums[row2 + 1][col1]
            - self.sums[row1][col2 + 1]
            + self.sums[row1][col1]
        )
