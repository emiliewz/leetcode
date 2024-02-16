# 153. Find Minimum in Rotated Sorted Array
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            if nums[l] < nums[h]:
                return nums[l]
            mid = l + (h - l) // 2
            # Left portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            # Right portion
            else:
                h = mid
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + (h - l) // 2
            # Left portion
            if nums[mid] > nums[h]:
                l = mid + 1
            # Right portion
            else:
                h = mid
        return nums[l]
