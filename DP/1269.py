# 1269. Number of Ways to Stay in the Same Place After Some Steps
from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(steps + 1, arrLen)
        a = [0] * (n + 1)
        a[0] = 1

        for _ in range(steps):
            left = 0
            for i in range(n):
                a[i], left = left + a[i] + a[i + 1], a[i]

        return a[0] % MOD


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(steps + 1, arrLen)
        a = [0] * n
        a[0] = 1

        for _ in range(steps):
            tmp = a[:] + [0]
            left = 0
            for i in range(n):
                a[i] = left + tmp[i] + tmp[i + 1]
                left = tmp[i]

        return a[0] % MOD


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(steps + 1, arrLen)
        a = [[0] * n for _ in range(steps + 1)]
        a[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(n):
                a[i][j] += a[i - 1][j]
                if j > 0:
                    a[i][j] += a[i - 1][j - 1]
                if j < n - 1:
                    a[i][j] += a[i - 1][j + 1]

        return a[steps][0] % MOD


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, k):
            if i < 0 or i >= arrLen:
                return 0
            if k == 0:
                return i == 0

            return (dp(i, k - 1) + dp(i + 1, k - 1) + dp(i - 1, k - 1)) % MOD

        return dp(0, steps)


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
