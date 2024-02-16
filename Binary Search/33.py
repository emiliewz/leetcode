# 33. Search in Rotated Sorted Array
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + ((h - l) >> 1)
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        if target < nums[0]:
            lo, hi = l, len(nums) - 1
        else:
            lo, hi = 0, l - 1 if l > 0 else len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
