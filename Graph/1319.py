# 1319. Number of Operations to Make Network Connected
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        k = len(connections)
        if k < n - 1:
            return -1
        p = list(range(n))
        rank = [1] * n
        res = n

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                p[p2] = p1
                rank[p1] += rank[p2]
            else:
                p[p1] = p2
                rank[p2] += rank[p1]
            return 1

        for i, j in connections:
            res -= union(i, j)

        return res - 1
