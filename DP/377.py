# 377. Combination Sum IV
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        a = [0] * (target + 1)
        a[0] = 1
        nums.sort()

        for i in range(target + 1):
            for n in nums:
                if n > i:
                    break
                a[i] += a[i - n]
        return a[target]
