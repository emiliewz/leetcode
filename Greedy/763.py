# 763. Partition Labels
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a = {}
        for i, j in enumerate(s):
            a[j] = i
        cur, size, res = 0, 0, []
        for i, j in enumerate(s):
            h = a[j]
            size += 1
            if h > cur:
                cur = h
            if i == cur:
                res.append(size)
                size = 0

        return res
