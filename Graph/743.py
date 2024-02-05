# 743. Network Delay Time
from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)

        for u, v, w in times:
            graph[u][v] = w
        h = [(0, k)]
        time = [float("inf")] * (n + 1)
        time[k] = 0

        while h:
            w, cur = heappop(h)
            for nei in graph[cur]:
                new_w = graph[cur][nei] + w
                if new_w < time[nei]:
                    time[nei] = new_w
                    heappush(h, (new_w, nei))
        maxTime = max(time[1:])
        return maxTime if maxTime != float("inf") else -1


# Dijkstra's algorithm
# Time complexity: O(E * log(V)), Space complexity: O(V + E)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i, j, w in times:
            graph[i].append((j, w))
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            cur_w, cur_node = heappop(minHeap)
            if cur_node in visit:
                continue
            visit.add(cur_node)
            t = max(t, cur_w)
            for node, weight in graph[cur_node]:
                if node not in visit:
                    heappush(minHeap, (weight + cur_w, node))
        return t if len(visit) == n else -1


# Floyd–Warshall algorithm
# Time complexity: O(N^3), Space complexity: O(N^2)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: {j: float("inf") for j in range(1, n + 1)} for i in range(1, n + 1)}
        for i, j, t in times:
            graph[i][j] = t

        for h in range(1, n + 1):
            graph[h][h] = 0
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    graph[i][j] = min(graph[i][j], graph[i][h] + graph[h][j])

        time = max(graph[k][i] for i in graph[k])
        return time if time != float("inf") else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: {j: float("inf") for j in range(1, n + 1)} for i in range(1, n + 1)}
        for i, j, t in times:
            graph[i][j] = t

        for i in range(1, n + 1):
            graph[i][i] = 0
            for j in range(1, n + 1):
                for h in range(1, n + 1):
                    if i != h:
                        graph[i][h] = min(graph[i][h], graph[i][j] + graph[j][h])
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for h in range(1, n + 1):
                    if i != h:
                        graph[i][h] = min(graph[i][h], graph[i][j] + graph[j][h])

        time = max(graph[k][i] for i in graph[k])
        return time if time != float("inf") else -1
