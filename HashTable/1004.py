# 1004. Max Consecutive Ones III
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for h, n in enumerate(nums):
            if not n:
                k -= 1
            if k < 0:
                if not nums[l]:
                    k += 1
                l += 1

        return h - l + 1
