# 213. House Robber II
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def house_robber(nums):
            nums += [0]
            for i in range(len(nums) - 3, -1, -1):
                nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            return nums[0]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))
