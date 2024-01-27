# 839. Similar String Groups
from collections import defaultdict
from itertools import combinations, permutations
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            p[px] = py
            return True

        def similar(i, j):
            f, s = strs[i], strs[j]
            i, count = 0, 0
            while i < m:
                if f[i] != s[i]:
                    count += 1
                    if count > 2:
                        return False
                i += 1
            return True

        n, m = len(strs), len(strs[0])
        p = [i for i in range(n)]
        res = n

        for i, j in combinations(range(n), 2):
            if similar(i, j):
                res -= union(i, j)

        return res


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] < rank[py]:
                p[px] = py
                rank[py] += rank[px]
            else:
                p[py] = px
                rank[px] += rank[py]
            return True

        def similar(i, j):
            f, s = strs[i], strs[j]
            i, count = 0, 0
            while i < m:
                if f[i] != s[i]:
                    count += 1
                    if count > 2:
                        return False
                i += 1
            return True

        n, m = len(strs), len(strs[0])
        p = [i for i in range(n)]
        rank = [1] * n

        for i, j in combinations(range(n), 2):
            if similar(i, j):
                union(i, j)

        res = [find(i) for i in range(n)]
        return len(set(res))
