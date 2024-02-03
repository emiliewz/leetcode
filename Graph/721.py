# 721. Accounts Merge
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            par[n1] = res
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True

        graph = {}

        for i, (_, *emails) in enumerate(accounts):
            for e in emails:
                if e in graph:
                    union(i, graph[e])
                graph[e] = i

        res = defaultdict(list)
        for email, i in graph.items():
            res[find(i)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if i != self.par[i]:
            self.par[i] = self.find(self.par[i])
        return self.par[i]

    def union(self, i, j):
        p1, p2 = self.find(i), self.find(j)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        graph = {}

        for i, (_, *emails) in enumerate(accounts):
            for e in emails:
                if e in graph:
                    uf.union(i, graph[e])
                graph[e] = i

        res = defaultdict(list)
        for email, idx in graph.items():
            res[uf.find(idx)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]
