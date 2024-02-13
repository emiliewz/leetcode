# 1140. Stone Game II
from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + piles[i - 1]

        @cache
        def dfs(i, m):
            total = sums[-1] - sums[i]
            if n - i <= 2 * m:
                return total
            res = 0
            for j in range(i + 1, min(i + 2 * m, n) + 1):
                res = max(res, total - dfs(j, max(m, j - i)))
            return res

        return dfs(0, 1)
