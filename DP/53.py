# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur = nums[0], 0

        for n in nums:
            cur = n + max(cur, 0)
            max_sum = max(cur, max_sum)

        return max_sum
