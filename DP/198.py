# 198. House Robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_sum = nums[:] + [0]
        for i in range(len(rob_sum) - 3, -1, -1):
            rob_sum[i] = max(rob_sum[i] + rob_sum[i + 2], rob_sum[i + 1])

        return rob_sum[0]
