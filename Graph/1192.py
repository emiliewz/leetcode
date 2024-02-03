# 1192. Critical Connections in a Network
from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        res = []
        root, par = [0] * n, [n] * n

        def dfs(i, k):
            root[i] = k

            for j in graph[i]:
                if par[i] == j:
                    continue
                if not root[j]:
                    par[j] = i
                    dfs(j, k + 1)
                    if root[j] > k:
                        res.append([i, j])
                root[i] = min(root[i], root[j])

        dfs(0, 1)
        return res


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        res = []
        root, par = [n] * n, [n] * n
        visit = [False] * n
        steps = 0

        def dfs(i):
            nonlocal steps
            visit[i] = True
            cur, root[i] = steps, steps
            steps += 1

            for j in graph[i]:
                if par[i] == j:
                    continue
                if not visit[j]:
                    par[j] = i
                    dfs(j)
                    if root[j] > cur:
                        res.append([i, j])
                root[i] = min(root[i], root[j])

        dfs(0)
        return res


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        connections = set([tuple(sorted(i)) for i in connections])
        rank = [-2] * n

        def dfs(i, k):
            if rank[i] >= 0:
                return rank[i]
            rank[i] = k
            min_back_depth = n

            for nei in graph[i]:
                if rank[nei] == k - 1:
                    continue
                back_depth = dfs(nei, k + 1)
                if back_depth <= k:
                    connections.discard(tuple(sorted((i, nei))))
                min_back_depth = min(back_depth, min_back_depth)
            rank[i] = n
            return min_back_depth

        dfs(0, 0)
        return list(connections)
