# 1269. Number of Ways to Stay in the Same Place After Some Steps
from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, k):
            if k == steps:
                return 1 if i == 0 else 0

            if i < 0 or i >= arrLen:
                return 0

            return (dp(i, k + 1) + dp(i + 1, k + 1) + dp(i - 1, k + 1)) % MOD

        return dp(0, 0) % MOD


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def dp(i, k):
            if (i, k) in memo:
                return memo[(i, k)]

            if k == steps:
                return 1 if i == 0 else 0

            if i < 0 or i >= arrLen:
                return 0

            memo[(i, k)] = dp(i, k + 1) + dp(i + 1, k + 1) + dp(i - 1, k + 1)
            return memo[(i, k)] % MOD

        return dp(0, 0) % MOD
