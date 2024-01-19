# 312. Burst Balloons
from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        a = [[0] * n for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i + 1, j):
                    a[i][j] = max(
                        a[i][j], a[i][k] + a[k][j] + nums[i] * nums[j] * nums[k]
                    )

        return a[0][n - 1]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(l, r):
            if l > r:
                return 0

            max_coins = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[r + 1] * nums[i]
                max_coins = max(max_coins, coins + dp(l, i - 1) + dp(i + 1, r))

            return max_coins

        nums = [1] + nums + [1]
        return dp(1, len(nums) - 2)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return nums[l - 1] * nums[l] * nums[l + 1]

            max_coins = 0
            for i in range(l, r + 1):
                max_coins = max(
                    nums[i] * nums[l - 1] * nums[r + 1] + dp(l, i - 1) + dp(i + 1, r),
                    max_coins,
                )
            return max_coins

        return dp(1, len(nums) - 2)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dp(l, r):
            if l > r:
                return 0

            max_coins = 0
            for i in range(l, r + 1):
                coins = (
                    nums[i] * nums[l - 1] * nums[r + 1] + dp(l, i - 1) + dp(i + 1, r)
                )
                max_coins = max(max_coins, coins)
            return max_coins

        return dp(1, len(nums) - 2)
