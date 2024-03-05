# 1139. Largest 1-Bordered Square
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        a = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1]:
                    a[i][j] = (a[i][j - 1][0] + 1, a[i - 1][j][1] + 1)
                    cur = min(a[i][j])
                    for k in range(cur, res, -1):
                        if a[i][j - k + 1][1] >= k and a[i - k + 1][j][0] >= k:
                            res = k

        return res**2
