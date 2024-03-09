# 218. The Skyline Problem


from heapq import heappop, heappush
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        a = []
        for i, j, h in buildings:
            a.append((i, -h, j))
            a.append((j, 0, 0))
        a.sort()
        maxHeap = [(0, float("inf"))]
        res = [(0, -1)]
        for left, h, right in a:
            while left >= maxHeap[0][1]:
                heappop(maxHeap)
            if h:
                heappush(maxHeap, (h, right))
            cur = -maxHeap[0][0]
            if res[-1][1] != cur:
                res.append((left, cur))

        return res[1:]
