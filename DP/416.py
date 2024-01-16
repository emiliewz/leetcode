# 416. Partition Equal Subset Sum
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1:
            return False
        target = sum(nums) >> 1
        nums.sort()

        @cache
        def dp(i, cur):
            if cur == target:
                return True
            if cur > target or i == len(nums):
                return False
            return dp(i + 1, cur + nums[i]) or dp(i + 1, cur)

        return dp(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]

        return dp[-1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort()
        target = total // 2
        memo = {}

        def dp(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if k == target:
                return True
            if i == len(nums):
                return False

            memo[(i, k)] = dp(i + 1, k + nums[i]) or dp(i + 1, k)
            return memo[(i, k)]

        return dp(0, 0)
