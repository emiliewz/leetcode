# 997. Find the Town Judge
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1

        t = [0] * (n + 1)

        for i, j in trust:
            t[i] -= 1
            t[j] += 1

        for i in range(1, n + 1):
            if t[i] == n - 1:
                return i

        return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        graph = defaultdict(set)
        judge = {i for i in range(1, n + 1)}
        for i, j in trust:
            graph[i].add(j)
        judge -= graph.keys()
        if not judge:
            return -1

        for p in graph:
            graph[p] -= graph.keys()
            if not graph[p]:
                return -1
        if len(judge) > 1:
            return -1
        return judge.pop()
