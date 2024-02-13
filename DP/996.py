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
                if not cur or isqrt(cur + nums[i]) ** 2 == cur + nums[i]:
                    dfs(nums[:i] + nums[i + 1 :], nums[i])

        res = 0
        nums.sort()
        dfs(nums, 0)
        return res
