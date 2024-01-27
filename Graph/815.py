# 815. Bus Routes
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for bus, route in enumerate(routes):
            for r in route:
                graph[r].add(bus)
        n = max(graph.keys())
        if source not in graph or target not in graph:
            return -1

        q = deque([source])
        visit = set([source])
        stops = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for bus in graph[cur]:
                    for nei in routes[bus]:
                        if nei not in visit:
                            if nei == target:
                                return stops
                            q.append(nei)
                            visit.add(nei)
            stops += 1
        return -1
