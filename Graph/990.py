# 990. Satisfiability of Equality Equations
from collections import defaultdict
from string import ascii_lowercase
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            p[p1] = p2

        p = {a: a for a in ascii_lowercase}

        for e in equations:
            a, b, sign = e[0], e[-1], e[1]
            if sign == "=":
                union(a, b)

        for e in equations:
            a, b, sign = e[0], e[-1], e[1]
            if sign == "!":
                if a == b or find(a) == find(b):
                    return False
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            p[p1] = p2

        p = list(range(26))
        inequal = defaultdict(set)

        for e in equations:
            a, b, sign = e[0], e[-1], e[1]
            if sign == "=":
                union(ord(a) - ord("a"), ord(b) - ord("a"))
            else:
                if a == b:
                    return False
                inequal[a].add(b)
                inequal[b].add(a)

        if not inequal:
            return True

        for a, k in inequal.items():
            for b in k:
                if find(ord(a) - ord("a")) == find(ord(b) - ord("a")):
                    return False
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = defaultdict(set)
        inequal = defaultdict(set)

        for i in equations:
            a, b = i[0], i[-1]
            match = i[1] == "="
            if match:
                equal[a].add(b)
                equal[b].add(a)
            else:
                if a == b:
                    return False
                inequal[a].add(b)
                inequal[b].add(a)

        for k in equal:
            for i in equal[k]:
                for j in equal[k]:
                    if j not in equal[i]:
                        equal[i].add(j)

        for a, b in equal.items():
            for c in b:
                if c in inequal[a]:
                    return False

        return True
