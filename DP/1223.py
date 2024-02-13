# 1223. Dice Roll Simulation
from functools import cache
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(cur, j, k):
            if k == n:
                return 1

            res = 0
            for i in range(6):
                if i != cur:
                    res += dp(i, 1, k + 1)
                elif j < rollMax[i]:
                    res += dp(i, j + 1, k + 1)
            return res

        return dp(-1, 0, 0) % MOD
