# 1. Two Sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in a:
                return [a[m], i]
            a[n] = i
        return None
