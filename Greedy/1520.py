# 1520. Maximum Number of Non-Overlapping Substrings
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # a: first seen index of letter
        # b: last seen index of letter
        first, a = {}, {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            a[c] = i
        res, start = [], -1

        # loop through last seen index of letter
        for i in sorted(a.values()):
            l = first[s[i]]
            r = j = i
            while j >= l and l > start and r == i:
                if l > first[s[j]]:
                    l = first[s[j]]
                if r < a[s[j]]:
                    r = a[s[j]]
                j -= 1
            if l > start and r == i:
                res.append(s[l : r + 1])
                start = r

        return res
