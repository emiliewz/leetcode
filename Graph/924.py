# 924. Minimize Malware Spread
from collections import Counter, defaultdict
from itertools import combinations
from typing import List


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            p[p2] = p1

        def safe(i):
            for j in initial:
                if par[i] == par[j] and i != j:
                    return False
            return True

        n = len(graph)
        p = list(range(n))
        for i, j in combinations(range(n), 2):
            if graph[i][j]:
                union(i, j)
        candidates = []

        initial.sort()
        par = [find(i) for i in range(n)]

        for i in initial:
            if safe(i):
                candidates.append(i)

        if not candidates:
            return initial[0]
        if len(candidates) == 1:
            return candidates[0]

        counts = Counter(par)
        a = {i: counts[par[i]] for i in candidates}
        max_connect = max(a.values())

        res = next(i for i, j in a.items() if j == max_connect)

        return res


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def hasConnect(i):
            for j in initial:
                if i != j:
                    if find(i) == find(j):
                        return True
            return False

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False

            if rank[p2] > rank[p1]:
                p[p1] = p2
                rank[p2] += rank[p1]
            else:
                p[p2] = p1
                rank[p1] += rank[p2]
            return True

        n = len(graph)
        p = list(range(n))
        rank = [1] * n
        for i, j in combinations(range(n), 2):
            if graph[i][j]:
                union(i, j)

        candidates = set()

        initial.sort()
        for node in initial:
            if not hasConnect(node):
                candidates.add(node)
        if not candidates:
            return initial[0]
        if len(candidates) == 1:
            return candidates.pop()

        counts = Counter(p)
        res = 0
        max_effort = 0
        for c in candidates:
            cur = counts[p[c]]
            if cur > max_effort:
                res = c
                max_effort = cur
            elif cur == max_effort:
                res = min(res, c)

        return res


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def hasConnect(i):
            for j in initial:
                if i != j:
                    if find(i) == find(j):
                        return True
            return False

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py

        n = len(graph)
        p = [i for i in range(n)]
        for i, j in combinations(range(n), 2):
            if graph[i][j]:
                union(i, j)

        candidates = set()

        initial.sort()
        for node in initial:
            if not hasConnect(node):
                candidates.add(node)
        if not candidates:
            return initial[0]
        if len(candidates) == 1:
            return candidates.pop()
        par = [find(i) for i in range(n)]
        counts = Counter(p)

        res = 0
        max_effort = 0
        for c in candidates:
            cur = counts[par[c]]
            if cur > max_effort:
                res = c
                max_effort = cur
            elif cur == max_effort:
                res = min(res, c)

        return res


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def hasConnect(i):
            for i in connections[i]:
                if i in initial:
                    return True
            return False

        n = len(graph)
        connections = defaultdict(set)
        for i, j in combinations(range(n), 2):
            if graph[i][j]:
                connections[i].add(j)
                connections[j].add(i)
        for i in connections:
            for j, k in combinations(connections[i], 2):
                if k not in connections[j]:
                    connections[j].add(k)
                    connections[k].add(j)
        candidates = set()

        initial.sort()
        for node in initial:
            if not hasConnect(node):
                candidates.add(node)

        if not candidates:
            return initial[0]

        res = set()
        max_effort = 0
        for c in candidates:
            if len(connections[c]) > max_effort:
                max_effort = len(connections[c])
                res.clear()
                res.add(c)
            elif len(connections[c]) == max_effort:
                res.add(c)

        return min(res)
