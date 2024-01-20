# 996. Number of Squareful Arrays
import math
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return math.isqrt(nums[0]) ** 2 == nums[0]
        res = 0
        nums.sort()

        def dfs(nums, cur):
            nonlocal res
            if not nums:
                res += 1
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if not cur or math.isqrt(nums[i] + cur) ** 2 == nums[i] + cur:
                    dfs(nums[:i] + nums[i + 1 :], nums[i])

        dfs(nums, "")
        return res


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        res = []
        nums.sort()

        def backtrack(nums, cur):
            if not nums:
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if (
                    len(cur) == 0
                    or (cur[-1] + nums[i]) == math.isqrt(cur[-1] + nums[i]) ** 2
                ):
                    backtrack(nums[:i] + nums[i + 1 :], cur + [nums[i]])

        backtrack(nums, [])
        return len(res)
