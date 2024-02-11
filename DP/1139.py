# 1139. Largest 1-Bordered Square
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        a = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1]:
                    a[i][j] = (a[i][j - 1][0] + 1, a[i - 1][j][1] + 1)
                    cur_max = min(a[i][j])
                    for k in range(cur_max, max_len, -1):
                        if a[i - k + 1][j][0] >= k and a[i][j - k + 1][1] >= k:
                            max_len = max(k, max_len)
                            break
        return max_len**2
