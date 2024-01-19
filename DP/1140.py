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
            if i + M >= n:
                return sums[i]
            stones = sums[i]

            max_stones = 0
            for x in range(1, 2 * M + 1):
                if i + x <= n:
                    max_stones = max(max_stones, stones - dp(i + x, max(x, M)))
            return max_stones

        return dp(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + piles[i - 1]

        @cache
        def dp(i, M):
            if i >= n:
                return 0

            stones = sum(piles[i:])
            max_stones = 0
            for x in range(1, 2 * M + 1):
                max_stones = max(max_stones, stones - dp(i + x, max(x, M)))
            return max_stones

        return dp(0, 1)


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
