# 451. Sort Characters By Frequency
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        a = defaultdict(int)

        for c in s:
            a[c] += 1

        return "".join(i * j for i, j in sorted(a.items(), key=lambda x: -x[1]))
