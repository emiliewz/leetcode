# 494. Target Sum
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums) + target
        tar = total >> 1
        if total & 1 or tar < 0:
            return 0

        a = [0] * (tar + 1)
        a[0] = 1
        nums.sort()

        for n in nums:
            if n > tar:
                return a[tar]
            for i in range(tar, n - 1, -1):
                a[i] += a[i - n]

        return a[tar]
