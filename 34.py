# 34. Find First and Last Position of Element in Sorted Array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(tar):
            l, h = 0, len(nums) - 1
            while l <= h:
                mid = l + (h - l) // 2
                if nums[mid] >= tar:
                    h = mid - 1
                else:
                    l = mid + 1
            return l

        left = search(target)
        right = search(target + 1) - 1

        if left <= right:
            return [left, right]
        return [-1, -1]
