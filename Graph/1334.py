# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        def dijkstra(x):
            h = [(0, x)]
            dist = [float("inf")] * n
            dist[x] = 0

            while h:
                d, i = heappop(h)
                if dist[i] > distanceThreshold:
                    break
                for nei, nei_d in graph[i]:
                    new_d = nei_d + d
                    if new_d <= dist[nei]:
                        dist[nei] = new_d
                        heappush(h, (new_d, nei))

            return sum(k <= distanceThreshold for k in dist) - 1

        graph = defaultdict(list)
        for i, j, k in edges:
            if k <= distanceThreshold:
                graph[i].append((j, k))
                graph[j].append((i, k))

        if len(graph) < n:
            return next(i for i in range(n - 1, -1, -1) if i not in graph)

        avaiable = []
        for i in graph:
            avaiable.append((dijkstra(i), i))

        avaiable.sort(key=lambda a: (a[0], -a[1]))
        return avaiable[0][1]
