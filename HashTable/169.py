# 169. Majority Element
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        tar = l // 2
        a = {}
        for n in nums:
            if n in a:
                a[n] += 1
            else:
                a[n] = 1
            if a[n] > tar:
                return n
        return 0
