# 611. Valid Triangle Number
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        k = 0
        for i in range(2, n):
            l, h = 0, i - 1
            while l < h:
                if nums[l] + nums[h] > nums[i]:
                    k += h - l
                    h -= 1
                else:
                    l += 1
        return k
