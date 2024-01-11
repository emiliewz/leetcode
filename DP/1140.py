# 1140. Stone Game II
from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sums[i] = sums[i + 1] + piles[i]

        @cache
        def dp(i, M):
            if i == n:
                return 0
            if i + 2 * M >= n:
                return sums[i]

            res = 0
            total_rest = sums[i]
            for j in range(1, 2 * M + 1):
                res = max(total_rest - dp(i + j, max(j, M)), res)
            return res

        return dp(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dp(i, M):
            if i == n:
                return 0
            if i + 2 * M >= n:
                return sum(piles[i:])

            res = 0
            total_rest = sum(piles[i:])
            for j in range(1, 2 * M + 1):
                res = max(total_rest - dp(i + j, max(j, M)), res)
            return res

        return dp(0, 1)
