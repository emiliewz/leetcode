# 1124. Longest Well-Performing Interval
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        cur, max_len = 0, 0
        a = {}
        for i, h in enumerate(hours):
            cur = cur + 1 if h > 8 else cur - 1
            if cur > 0:
                max_len = i + 1
            if cur not in a:
                a[cur] = i
            if cur - 1 in a:
                max_len = max(max_len, i - a[cur - 1])

        return max_len
