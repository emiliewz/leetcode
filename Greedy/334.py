# 334. Increasing Triplet Subsequence
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = s = float("inf")
        for n in nums:
            if n > s:
                return True
            if n <= f:
                f = n
            else:
                s = n

        return False
