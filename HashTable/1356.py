# 1356. Sort Integers by The Number of 1 Bits
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def byBits(n):
            bit_count = bin(n).count("1")
            return (bit_count, n)

        arr.sort(key=byBits)
        return arr


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(x):
            res = 0
            while x:
                x &= x - 1
                res += 1
            return res

        arr.sort(key=lambda x: (countBits(x), x))
        return arr
