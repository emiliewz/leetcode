# 162. Find Peak Element
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float("inf")] + nums + [-float("inf")]
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] > nums[mid - 1]:
                if nums[mid] > nums[mid + 1]:
                    return mid - 1
                else:
                    l = mid + 1
            else:
                h = mid

        return l - 1
