# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        for i in range(n - 1):
            cur = 0
            for j in range(i, n):
                cur ^= arr[j]
                if not cur:
                    res += j - i
        return res
