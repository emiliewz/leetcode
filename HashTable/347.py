# 347. Top K Frequent Elements
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        for n in nums:
            a[n] += 1
        candidates = sorted(a.items(), key=lambda x: -x[1])
        cur, res = 0, []
        for i, j in enumerate(candidates):
            if i == 0 or j[0] != candidates[i - 1][0]:
                cur += 1
            res.append(j[0])
            if cur >= k:
                return res
