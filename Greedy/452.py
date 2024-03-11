# 452. Minimum Number of Arrows to Burst Balloons
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        k, r = 0, -float("inf")
        for l, h in points:
            if l > r:
                k += 1
                r = h
        return k
