# 1011. Capacity To Ship Packages Within D Days
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(x):
            count, cur = 1, 0
            for w in weights:
                if cur + w <= x:
                    cur += w
                else:
                    cur = w
                    count += 1
            return count <= days

        l = max(weights)
        if days == len(weights):
            return l
        h = sum(weights)

        while l < h:
            mid = l + (h - l) // 2
            if canShip(mid):
                h = mid
            else:
                l = mid + 1

        return l
