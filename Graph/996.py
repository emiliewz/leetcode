# 996. Number of Squareful Arrays
from math import isqrt
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def dfs(nums, cur):
            if not nums:
                nonlocal res
                res += 1
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if not cur or isqrt(cur[-1] + nums[i]) ** 2 == cur[-1] + nums[i]:
                    dfs(nums[:i] + nums[i + 1 :], cur + [nums[i]])

        res = 0
        nums.sort()
        dfs(nums, [])
        return res


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def dfs(nums, cur):
            if len(cur) == n:
                nonlocal res
                res += 1
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if not cur or isqrt(nums[i] + cur[-1]) ** 2 == nums[i] + cur[-1]:
                    dfs(nums[:i] + nums[i + 1 :], cur + [nums[i]])

        nums.sort()
        n = len(nums)
        res = 0
        dfs(nums, [])
        return res
