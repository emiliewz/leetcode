# 1437. Check If All 1's Are at Least Length K Places Away
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = -float("inf")
        for cur, n in enumerate(nums):
            if n:
                if cur - i <= k:
                    return False
                i = cur
        return True
