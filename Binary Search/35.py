# 35. Search Insert Position
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return h

        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] >= target:
                h = mid - 1
            else:
                l = mid + 1

        return l
