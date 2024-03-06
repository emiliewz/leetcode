# 1493. Longest Subarray of 1's After Deleting One Element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        k = 1
        for h, n in enumerate(nums):
            if not n:
                k -= 1
            if k < 0:
                if not nums[l]:
                    k += 1
                l += 1
        return h - l


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        cur, res = 0, 0
        a = (-1, 0)
        for i, n in enumerate(nums):
            if n:
                cur += 1
                res = max(cur, res)
            else:
                left = i - cur
                if a[0] == left - 1:
                    res = max(res, a[1] + cur)
                a = (i, cur)
                cur = 0

        return min(res, len(nums) - 2)
