# 391. Perfect Rectangle
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        a = lambda: (y2 - y1) * (x2 - x1)

        for x1, y1, x2, y2 in rectangles:
            area += a()
            corners ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}

        if len(corners) != 4:
            return False

        x1, y1 = min(corners, key=lambda x: x[0] + x[1])
        x2, y2 = max(corners, key=lambda x: x[0] + x[1])

        return a() == area
