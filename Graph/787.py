# 787. Cheapest Flights Within K Stops
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        h = [(0, 0, src)]
        price = [float("inf")] * n

        while h:
            c, w, cur = heappop(h)

            if c <= k:
                for nei in graph[cur]:
                    new_price = w + graph[cur][nei]
                    if new_price < price[nei]:
                        price[nei] = new_price
                        heappush(h, (c + 1, new_price, nei))

        return price[dst] if price[dst] != float("inf") else -1


# Bellman-Ford algorithm
# Time complexity: O(E * K)
# Space complexity: O(n)
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[:]
            update = False
            for i, j, p in flights:
                if tmp[i] + p < prices[j]:
                    prices[j] = tmp[i] + p
                    update = True

            if not update:
                break

        return prices[dst] if prices[dst] != float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        minHeap = [(0, 0, src)]
        t = float("inf")
        visit = set()

        while minHeap:
            c, weight, node = heappop(minHeap)
            if node == dst:
                t = min(t, weight)
                continue

            for nei_n, nei_w in graph[node]:
                if c < k + 1 and (c, node, nei_n) not in visit:
                    visit.add((c, node, nei_n))
                    heappush(minHeap, (c + 1, weight + nei_w, nei_n))

        return t if t != float("inf") else -1
