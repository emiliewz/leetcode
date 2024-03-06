# 2564. Substring XOR Queries
from collections import defaultdict
from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        a = defaultdict(lambda: [-1, -1])
        n = len(s)
        for i in range(n):
            if s[i] == "0":
                if 0 not in a:
                    a[0] = [i, i]
                continue
            k = 0
            for j in range(i, min(i + 30, n)):
                k <<= 1
                if s[j] == "1":
                    k |= 1
                if k not in a:
                    a[k] = [i, j]

        return [a[i ^ j] for i, j in queries]
