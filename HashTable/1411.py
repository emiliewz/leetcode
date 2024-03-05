# 1411. Number of Ways to Paint N × 3 Grid
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        f, s = 6, 6
        for _ in range(n - 1):
            f, s = f * 3 + s * 2, f * 2 + s * 2

        return (f + s) % MOD
