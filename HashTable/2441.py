# 2441. Largest Positive Integer That Exists With Its Negative
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        print("num", num)
        while num:
            cur = num.pop()
            if cur < 0:
                return -1
            if -cur in num:
                return cur
        return -1
