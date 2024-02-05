# 882. Reachable Nodes In Subdivided Graph
from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(set)
        for u, v, w in edges:
            graph[u].add((v, w + 1))
            graph[v].add((u, w + 1))
        dist = [float("inf")] * n
        dist[0] = 0

        h = [(0, 0)]
        while h:
            cur_d, cur = heappop(h)
            for i, d in graph[cur]:
                new_d = cur_d + d
                if new_d < dist[i]:
                    dist[i] = new_d
                    heappush(h, (new_d, i))
        res = sum(d <= maxMoves for d in dist)

        for u, v, w in edges:
            k = 0
            if dist[v] < maxMoves:
                k += maxMoves - dist[v]
            if dist[u] < maxMoves:
                k += maxMoves - dist[u]
            res += min(k, w)

        return res


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(set)
        dist = [float("inf")] * n
        dist[0] = 0
        for i, j, w in edges:
            graph[i].add((j, w + 1))
            graph[j].add((i, w + 1))

        minHeap = [(0, 0)]

        while minHeap:
            cur_d, cur_i = heappop(minHeap)
            if dist[cur_i] > maxMoves:
                break
            for i, d in graph[cur_i]:
                new_d = cur_d + d
                if new_d < dist[i]:
                    dist[i] = new_d
                    heappush(minHeap, (new_d, i))

        res = sum(d <= maxMoves for d in dist)

        for i, j, w in edges:
            w1, w2 = max(maxMoves - dist[i], 0), max(maxMoves - dist[j], 0)
            res += min(w1 + w2, w)

        return res


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        a = {}
        graph = defaultdict(list)
        for i, j, k in edges:
            graph[i].append((j, k))
            graph[j].append((i, k))
            a[(i, j)] = set(range(k))
            a[(j, i)] = set(range(k))

        q, reachable = deque([(maxMoves, 0)]), 0
        visit = set()
        while q:
            k, cur = q.popleft()
            visit.add(cur)
            if k > 0:
                for nei_node, nextmove in graph[cur]:
                    for i in range(k):
                        if i in a[(cur, nei_node)]:
                            reachable += 1
                            a[(cur, nei_node)].remove(i)
                            a[(nei_node, cur)].remove(nextmove - 1 - i)
                    if k - nextmove > 0:
                        q.append((k - nextmove - 1, nei_node))

        return reachable + len(visit)


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        a = {}
        graph = defaultdict(list)
        for i, j, k in edges:
            graph[i].append((j, k))
            graph[j].append((i, k))
            a[(i, j)] = set(range(k))

        q, reachable = [(maxMoves, 0)], 0
        visit = set()
        seen = [0] * n
        seen[0] = maxMoves
        while q:
            k, cur = heappop(q)
            visit.add(cur)
            for nei_node, nextmove in graph[cur]:
                if (cur, nei_node) in a:
                    for i in set(a[(cur, nei_node)]):
                        if i < k:
                            reachable += 1
                            a[(cur, nei_node)].remove(i)
                else:
                    for i in set(a[(nei_node, cur)]):
                        if i >= nextmove - k:
                            reachable += 1
                            a[(nei_node, cur)].remove(i)
                if k >= nextmove:
                    a[(cur, nei_node)] = set()
                    if k > nextmove:
                        visit.add(nei_node)
                    if k > nextmove + 1 and seen[nei_node] < k - nextmove - 1:
                        seen[nei_node] = k - nextmove - 1
                        heappush(q, (k - nextmove - 1, nei_node))

        return reachable + len(visit)
