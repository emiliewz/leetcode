# 1202. Smallest String With Swaps
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(i, j):
            p1, p2 = find(i), find(j)
            p[p1] = p2

        n = len(s)
        p = list(range(n))
        for i, j in pairs:
            union(i, j)

        finds = [find(i) for i in range(n)]
        dicts = defaultdict(list)
        for i in range(n):
            par = find(i)
            dicts[par].append(s[i])

        for d in dicts:
            dicts[d].sort(reverse=True)
        res = ""
        for i in range(n):
            par = find(i)
            res += dicts[par].pop()
        return res


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py

        n = len(s)
        p = [i for i in range(n)]

        for x, y in pairs:
            union(x, y)

        a = defaultdict(list)

        for i, e in enumerate(p):
            a[find(e)].append(i)

        res = list(s)
        for key in a.keys():
            i_list = a[key]
            char_list = [s[i] for i in i_list]
            char_list.sort()

            for idx, char in zip(i_list, char_list):
                res[idx] = char

        return "".join(res)
