# 303. Range Sum Query - Immutable
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sums = [0] * (n + 1)
        for i in range(1, n + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
