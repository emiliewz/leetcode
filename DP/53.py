# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur = 0

        for n in nums:
            cur = max(0, cur) + n
            max_sub = max(max_sub, cur)

        return max_sub
