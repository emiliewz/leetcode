# 996. Number of Squareful Arrays
import math
from typing import List


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
