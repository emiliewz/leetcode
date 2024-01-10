# 1223. Dice Roll Simulation
from functools import cache
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(rolls, j, k):
            if rolls == n:
                return 1
            res = 0
            for i in range(6):
                if i == j:
                    if k < rollMax[i]:
                        res += dp(rolls + 1, i, k + 1)
                else:
                    res += dp(rolls + 1, i, 1)
            return res % MOD

        return dp(0, -1, 0) % MOD


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(k, prev_num, prev_times):
            if k == n:
                return 1
            res = 0
            for i in range(1, 7):
                if i == prev_num:
                    if prev_times < rollMax[i - 1]:
                        res += dp(k + 1, i, prev_times + 1)
                else:
                    res += dp(k + 1, i, 1)

            return res % MOD

        return dp(0, 0, 0) % MOD
