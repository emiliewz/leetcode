# 494. Target Sum
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        if sums < abs(target) or (sums + target) & 1:
            return 0
        new_target = (target + sums) >> 1
        a = [0] * (new_target + 1)
        a[0] = 1

        for n in nums:
            for i in range(new_target, n - 1, -1):
                a[i] += a[i - n]

        return a[new_target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, cur):
            if i == len(nums):
                return int(cur == target)
            return dp(i + 1, cur - nums[i]) + dp(i + 1, cur + nums[i])

        return dp(0, 0)


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
