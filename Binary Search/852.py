# 852. Peak Index in a Mountain Array
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 0, len(arr) - 1

        while l < h:
            mid = l + (h - l) // 2
            # Left portion
            if arr[mid] > arr[mid - 1]:
                if arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    l = mid + 1
            # Right portion
            else:
                h = mid
        return l
