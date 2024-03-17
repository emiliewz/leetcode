# 2242. Maximum Score of a Node Sequence
from heapq import nlargest
from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        a = [[] for i in range(n)]
        for i, j in edges:
            a[i].append((scores[j], j))
            a[j].append((scores[i], i))
        for i in range(n):
            a[i] = nlargest(3, a[i])
        res = -1
        for i, j in edges:
            for k, h in a[i]:
                for m, n in a[j]:
                    if h != j and i != n and h != n:
                        res = max(res, k + m + scores[i] + scores[j])
        return res
