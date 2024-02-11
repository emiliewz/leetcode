# 1187. Make Array Strictly Increasing
from bisect import bisect_right
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        n = len(arr2)
        a = {-1: 0}

        for i in arr1:
            tmp = a.copy()
            a = {}
            for k in tmp:
                if i > k:
                    a[i] = min(a.get(i, float("inf")), tmp[k])
                j = bisect_right(arr2, k)
                if j < n:
                    a[arr2[j]] = min(a.get(arr2[j], float("inf")), tmp[k] + 1)

        return min(a.values()) if a else -1
