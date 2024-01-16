# 1049. Last Stone Weight II
from functools import cache
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        if n == 2:
            return abs(stones[0] - stones[1])
        sums = sum(stones)
        target = sums >> 1
        a = [False] * (target + 1)
        a[0] = True
        stones.sort()

        for s in stones:
            for i in range(target, s - 1, -1):
                a[i] = a[i] or a[i - s]

        for i in range(target, -1, -1):
            if a[i]:
                return sums - 2 * i

        return 0


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for s in stones:
            for i in range(target, s - 1, -1):
                dp[i] = dp[i] or dp[i - s]

        for i in range(target, -1, -1):
            if dp[i]:
                return total_sum - 2 * i


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        dp = [0] * (target + 1)

        for s in stones:
            for i in range(target, s - 1, -1):
                dp[i] = max(dp[i], dp[i - s] + s)

        return total_sum - 2 * dp[target]


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dp(i, total):
            if i == len(stones):
                return abs(total)
            return min(dp(i + 1, total - stones[i]), dp(i + 1, total + stones[i]))

        return dp(0, 0)
