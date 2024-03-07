# 1488. Avoid Flood in The City
from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        dayToFill = SortedList()
        fullLakes = {}
        for i, r in enumerate(rains):
            if not r:
                dayToFill.add(i)
            else:
                if r in fullLakes:
                    j = dayToFill.bisect_right(fullLakes[r])
                    if j == len(dayToFill):
                        return []
                    res[dayToFill[j]] = r
                    dayToFill.pop(j)
                fullLakes[r] = i

        while dayToFill:
            i = dayToFill.pop()
            res[i] = 1
        return res
