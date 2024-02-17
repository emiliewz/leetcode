# 719. Find K-th Smallest Pair Distance
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, h = 0, nums[-1] - nums[0]
        while l < h:
            mid = l + ((h - l) >> 1)
            count = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] <= nums[i] + mid:
                    j += 1
                count += j - i - 1

            if count < k:
                l = mid + 1
            else:
                h = mid
        return l
