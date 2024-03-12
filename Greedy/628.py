# 628. Maximum Product of Three Numbers
from heapq import nlargest, nsmallest
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b = nlargest(3, nums), nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])
