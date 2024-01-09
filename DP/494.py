# 494. Target Sum
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, k):
            if (i, k) in memo:
                return memo[(i, k)]

            if i == len(nums):
                return 1 if k == target else 0

            memo[(i, k)] = dp(i + 1, k + nums[i]) + dp(i + 1, k - nums[i])
            return memo[(i, k)]

        return dp(0, 0)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, k):
            if i == len(nums):
                return 1 if k == target else 0

            return dp(i + 1, k + nums[i]) + dp(i + 1, k - nums[i])

        return dp(0, 0)
