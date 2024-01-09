# 1139. Largest 1-Bordered Square
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_len = 0

        # (x, y) in dp, refer to the accumulative width, height
        dp = [[(0, 0)] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            if grid[i - 1][0]:
                max_len = 1
                dp[i][1] = (1, dp[i - 1][1][1] + 1)

        for i in range(1, n + 1):
            if grid[0][i - 1]:
                max_len = 1
                dp[1][i] = (dp[1][i - 1][0] + 1, 1)

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                if grid[i - 1][j - 1]:
                    dp[i][j] = (dp[i][j - 1][0] + 1, dp[i - 1][j][1] + 1)
                    for k in range(min(dp[i][j]), max_len, -1):
                        if min(dp[i - k + 1][j][0], dp[i][j - k + 1][1]) >= k:
                            max_len = k
        return max_len**2
