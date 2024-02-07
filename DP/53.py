# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur = nums[0], 0

        for n in nums:
            cur = n + max(cur, 0)
            max_sum = max(cur, max_sum)

        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur = 0

        for n in nums:
            cur = max(0, cur) + n
            max_sub = max(max_sub, cur)

        return max_sub


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, max_sum = 0, nums[0]

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            max_sum = max(max_sum, cur)

        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            max_sum = max(max_sum, cur)

        return max_sum
