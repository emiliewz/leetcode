# 740. Delete and Earn
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        a = [0] * (nums[-1] + 1)
        for i in nums:
            a[i] += 1

        f, s = 0, 0
        for i in range(nums[-1], -1, -1):
            f, s = max(i * a[i] + s, f), f

        return f

