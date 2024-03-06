# 2134. Minimum Swaps to Group All 1's Together II
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        zeros = 0
        n = len(nums)
        for i in range(k):
            if not nums[i]:
                zeros += 1
        l = 0
        res = n
        for i in range(k, n + k):
            if not nums[l % n]:
                zeros -= 1
            if not nums[i % n]:
                zeros += 1
            res = min(res, zeros)
            l += 1
        return res
