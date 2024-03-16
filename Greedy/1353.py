# 1353. Maximum Number of Events That Can Be Attended
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        minH = []
        res = 0
        i = 0
        while events or minH:
            if not minH:
                i = events[-1][0]
            while events and events[-1][0] <= i:
                heapq.heappush(minH, events.pop()[1])
            heapq.heappop(minH)
            res += 1
            i += 1
            while minH and minH[0] < i:
                heapq.heappop(minH)
        return res
