# 128. Longest Consecutive Sequence
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l
        a = set(nums)
        res = 1
        for n in a:
            if n - 1 in a:
                continue
            cur = 1
            while n + 1 in a:
                cur += 1
                n += 1
            res = max(res, cur)

        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        nums.sort()
        cur, res = 1, 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1

        return res
