# 213. House Robber II
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            f, s = 0, 0
            for i in range(len(nums)):
                f, s = max(nums[i] + s, f), f

            return f

        if len(nums) == 1:
            return nums[0]

        return max(robber(nums[1:]), robber(nums[:-1]))
