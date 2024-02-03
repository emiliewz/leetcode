
# 332. Reconstruct Itinerary
from collections import defaultdict
from typing import List


# Euler path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        a = defaultdict(list)
        tickets.sort(reverse=True)
        for i, j in tickets:
            a[i].append(j)
        res = []

        def dfs(i):
            while a[i]:
                dfs(a[i].pop())
            res.append(i)

        dfs("JFK")
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        tickets.sort()
        graph = defaultdict(list)
        for i, j in tickets:
            graph[i].append(j)
        res = ["JFK"]

        def dfs(src):
            if len(res) == n + 1:
                return True
            if src not in graph:
                return False
            for i, j in enumerate(graph[src][:]):
                graph[src].pop(i)
                res.append(j)
                if dfs(j):
                    return True
                graph[src].insert(i, j)
                res.pop()

            return False

        dfs("JFK")
        return res
