# 154. Find Minimum in Rotated Sorted Array II
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + (h - l) // 2

            # Left portion
            if nums[mid] > nums[h]:
                l = mid + 1
            # Right portion
            elif nums[mid] < nums[h]:
                h = mid
            else:
                h -= 1
                while h >= mid and nums[h] == nums[h - 1]:
                    h -= 1

        return nums[l]
