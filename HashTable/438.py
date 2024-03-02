# 438. Find All Anagrams in a String
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        sCount, pCount = defaultdict(int), defaultdict(int)

        for i, j in enumerate(p):
            sCount[s[i]] += 1
            pCount[j] += 1
        res = [0] if sCount == pCount else []
        l = 0
        for r in range(m, n):
            sCount[s[r]] += 1
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res
