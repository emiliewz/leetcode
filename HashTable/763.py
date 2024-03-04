# 763. Partition Labels
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a, res = {}, []
        for i, c in enumerate(s):
            a[c] = i

        size, cur = 0, 0
        for i, c in enumerate(s):
            size += 1
            cur = max(cur, a[c])
            if i == cur:
                res.append(size)
                size = 0
        return res
