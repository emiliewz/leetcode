# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k = nums.count(1)
        n = len(nums)
        if k:
            return n - k

        for i in range(n):
            for j in range(n - i - 1):
                nums[j] = gcd(nums[j], nums[j + 1])
                if nums[j] == 1:
                    return i + n
        return -1
