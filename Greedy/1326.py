# 1326. Minimum Number of Taps to Open to Water a Garden
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        a = [0] * (n + 1)
        for i, r in enumerate(ranges):
            l = max(0, i - r)
            a[l] = max(a[l], i + r)

        res = 0
        l = r = 0
        while r < n:
            l, r = r, max(a[l : r + 1])
            if r <= l:
                return -1
            res += 1
        return res


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        a = [float("inf")] * (n + 1)
        a[0] = 0

        for i, x in enumerate(ranges):
            if x != 0:
                start, end = max(0, i - x), min(i + x, n)
                for j in range(start + 1, end + 1):
                    a[j] = min(a[j], a[start] + 1)
        return a[-1] if a[-1] != float("inf") else -1


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        a = sorted([i - r, i + r] for i, r in enumerate(ranges))
        res = 0
        l = r = 0
        i = 0
        while r < n:
            while i <= n and a[i][0] <= l:
                r = max(r, a[i][1])
                i += 1
            if r <= l:
                return -1
            res += 1
            l = r
        return res
