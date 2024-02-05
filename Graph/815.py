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
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        if source not in graph or target not in graph:
            return -1

        q = deque([target])
        stops = 0
        visit = set()
        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                for bus in graph[cur]:
                    if bus not in visit:
                        for i in routes[bus]:
                            if i == source:
                                return stops + 1
                            visit.add(bus)
                            q.append(i)
            stops += 1
        return -1


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
