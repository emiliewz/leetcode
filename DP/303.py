# 303. Range Sum Query - Immutable
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = nums[i] + self.sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # return self.sums[right] - self.sums[left-1] if left >= 1 else self.sums[right]
        if left > 0 and right > 0:
            return self.sums[right] - self.sums[left - 1]
        print(left or right, self.sums[left or right])
        return self.sums[left or right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
