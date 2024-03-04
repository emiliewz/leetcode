# 792. Number of Matching Subsequences
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        a = defaultdict(list)

        for w in words:
            a[w[0]].append(w[1:])

        res = 0
        for c in s:
            cur = a.pop(c, [])
            for i in cur:
                if not i:
                    res += 1
                else:
                    a[i[0]].append(i[1:])

        return res
