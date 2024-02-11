# 416. Partition Equal Subset Sum
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        target = sums // 2
        nums.sort()
        if sums % 2 or nums[-1] > target:
            return False
        if nums[-1] == target:
            return True

        a = [False] * (target + 1)
        a[0] = True

        for n in nums:
            if n > target:
                break
            for i in range(target, n - 1, -1):
                a[i] = a[i] or a[i - n]
        return a[-1]
