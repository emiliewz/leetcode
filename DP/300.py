# 300. Longest Increasing Subsequence
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        a = []

        for n in nums:
            if not a or n > a[-1]:
                a.append(n)
            else:
                pos = bisect_left(a, n)
                a[pos] = n
        return len(a)
