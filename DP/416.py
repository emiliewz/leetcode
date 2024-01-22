# 416. Partition Equal Subset Sum
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        nums.sort()
        target = sums // 2
        if sums % 2 or nums[-1] > target:
            return False
        if nums[-1] == target:
            return True

        a = [False] * (target + 1)
        a[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                a[i] = a[i] or a[i - num]

        return a[target]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        nums.sort()
        target = sums // 2
        if sums % 2 or nums[-1] > target:
            return False
        n = len(nums)

        @cache
        def dp(i, cur):
            if cur == target:
                return True
            if i == n:
                return False

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                if nums[j] + cur <= target:
                    if dp(j + 1, cur + nums[j]):
                        return True
            return False

        return dp(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        nums.sort(reverse=True)
        target = sums // 2
        if sums % 2 or nums[0] > target:
            return False
        n = len(nums)
        a = [0] * 2

        def dfs(i):
            if i == n:
                return True

            for j in range(2):
                if a[j] + nums[i] <= target:
                    a[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    a[j] -= nums[i]
                    if a[j] == 0:
                        return False
            return False

        return dfs(0)


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
