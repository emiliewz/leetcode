# 1269. Number of Ways to Stay in the Same Place After Some Steps
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(arrLen, steps + 1)
        a = [0] * (n + 1)
        a[0] = 1

        for _ in range(steps):
            left = 0
            for i in range(n):
                a[i], left = left + a[i] + a[i + 1], a[i]

        return a[0] % MOD
