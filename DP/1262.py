# 1262. Greatest Sum Divisible by Three
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [0, 0, 0]
        for i in nums:
            for j in a[:]:
                a[(i + j) % 3] = max(a[(i + j) % 3], i + j)
        return a[0]
