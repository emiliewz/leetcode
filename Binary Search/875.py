# 875. Koko Eating Bananas
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def canEat(x):
            count = 0
            for pile in piles:
                count += ceil(pile / x)
            if count > H:
                return False
            return True

        l, h = 1, max(piles)
        if H == len(piles):
            return h

        while l < h:
            mid = l + (h - l) // 2
            if canEat(mid):
                h = mid
            else:
                l = mid + 1

        return l
