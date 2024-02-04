# 399. Evaluate Division
from collections import defaultdict, deque
from itertools import combinations
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for idx, (i, j) in enumerate(equations):
            graph[i][j] = values[idx]
            graph[j][i] = 1 / values[idx]

        for i in graph:
            graph[i][i] = 1
            for j, k in combinations(graph[i], 2):
                if j not in graph[k]:
                    graph[k][j] = graph[k][i] * graph[i][j]
                    graph[j][k] = graph[j][i] * graph[i][k]

        return [
            graph[i][j] if (i in graph and j in graph[i]) else -1 for i, j in queries
        ]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(values)):
            u, v = equations[i]
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    if j not in graph[i]:
                        graph[i][j] = graph[i][k] * graph[k][j]

        return [
            graph[u][v] if (u in graph and v in graph[u]) else -1 for u, v in queries
        ]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        a = defaultdict(list)

        for i, j in enumerate(equations):
            u, v = j
            a[u].append((v, values[i]))
            a[v].append((u, 1 / values[i]))

        def bfs(src, target):
            if src not in a or target not in a:
                return -1
            if src == target:
                return 1

            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                c, v = q.popleft()
                if c == target:
                    return v

                for char, value in a[c]:
                    if char not in visit:
                        q.append([char, value * v])
                        visit.add(char)
            return -1

        return [bfs(i, j) for i, j in queries]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(values)):
            u, v = equations[i]
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j] if i != j else 1

        return [graph[u][v] if v in graph[u] else -1 for u, v in queries]
