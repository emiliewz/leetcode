# 213. House Robber II
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n <= 3:
            return max(nums)

        def house_rob(nums):
            f, s = nums[-1], 0
            for i in range(len(nums) - 2, -1, -1):
                f, s = max(nums[i] + s, f), f
            return f

        return max(house_rob(nums[1:]), house_rob(nums[:-1]))


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
