# 692. Top K Frequent Words
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a = defaultdict(int)
        for word in words:
            a[word] += 1
        res = []
        cur = sorted(a.items(), key=lambda x: (-x[1], x[0]))
        for _ in range(k):
            res.append(cur.pop(0)[0])

        return res
