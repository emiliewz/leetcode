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


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        a = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    a[i] = max(a[i], a[j] + 1)

        return max(a)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        len_lts = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    len_lts[i] = max(len_lts[i], len_lts[j] + 1)

        return max(len_lts)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lts = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lts[i] = max(lts[i], lts[j] + 1)

        return max(lts)
