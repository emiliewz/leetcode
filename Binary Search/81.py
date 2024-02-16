# 81. Search in Rotated Sorted Array II
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, h = 0, len(nums) - 1
        while l <= h:
            m = l + ((h - l) >> 1)
            if target == nums[m]:
                return True
            if nums[l] == nums[m]:
                l += 1
                while l <= m and nums[l] == nums[l + 1]:
                    l += 1
            # Left portion
            elif nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            # Right portion
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1

        return False
