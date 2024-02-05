# 685. Redundant Connection II
from collections import defaultdict, deque
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i: [] for i in range(1, n + 1)}
        froms = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            froms[j].append(i)

        ends = [i for i in range(1, n + 1) if not graph[i]]
        candidates = [i for i in froms if len(froms[i]) > 1]

        q = deque(ends)
        while q:
            cur = q.popleft()
            for nei in froms[cur]:
                graph[nei].remove(cur)
                if not graph[nei]:
                    q.append(nei)
            froms.pop(cur)
        haveCircle = False if not froms else True

        # not circle
        if not haveCircle:
            for i, j in edges[::-1]:
                if j in candidates:
                    return [i, j]

        # must have a circle
        if not candidates:
            for i, j in edges[::-1]:
                if i in froms and j in froms:
                    return [i, j]

        # have duplicate
        for i, j in edges[::-1]:
            if j in candidates and i in froms and j in froms[i]:
                return [i, j]
        for i, j in edges[::-1]:
            if j in candidates and i in froms:
                return [i, j]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def break_loop():
            q = deque(ends)
            while q:
                i = q.popleft()
                for nei in froms[i]:
                    graph[nei].remove(i)
                    if not graph[nei]:
                        q.append(nei)
                froms.pop(i)
            if not froms:
                return False
            return True

        n = len(edges)
        graph = defaultdict(set)
        froms = {i: set() for i in range(1, n + 1)}
        for i, j in edges:
            graph[i].add(j)
            froms[j].add(i)

        ends = [i for i in range(1, n + 1) if i not in graph]
        duplicate = next((i for i in range(1, n + 1) if len(froms[i]) > 1), 0)
        breakLoop = break_loop()

        if not duplicate:  # have loop
            return next([i, j] for i, j in edges[::-1] if i in graph and j in graph[i])

        if duplicate in ends or not breakLoop:  # have no loop
            return next([i, j] for i, j in edges[::-1] if j == duplicate)

        # have duplicate, have loop and break it
        # have exactly a loop invloves two elements
        for i, j in edges[::-1]:
            if j == duplicate and i in graph[j]:
                return [i, j]

        # have a loop invloves more elements
        for i, j in edges[::-1]:
            if j == duplicate and (i in froms and froms[i]):
                return [i, j]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(set)
        froms = {i: set() for i in range(1, n + 1)}
        for i, j in edges:
            graph[i].add(j)
            froms[j].add(i)

        end = [i for i in range(1, n + 1) if i not in graph]
        root = next((i for i in range(1, n + 1) if not froms[i]), 0)
        duplicate = next((i for i in range(1, n + 1) if len(froms[i]) > 1), 0)
        if duplicate:
            if duplicate in end:
                for i, j in edges[::-1]:
                    if j == duplicate:
                        return [i, j]
            else:
                q = deque(end)
                while q:
                    i = q.popleft()
                    for nei in froms[i]:
                        graph[nei].remove(i)
                        if not graph[nei]:
                            q.append(nei)
                    froms.pop(i)
                if not froms:
                    for i, j in edges[::-1]:
                        if j == duplicate:
                            return [i, j]
                q.append(root)
                while q:
                    i = q.popleft()
                    for nei in graph[i]:
                        froms[nei].remove(i)
                        if not froms[nei]:
                            q.append(nei)
                    graph.pop(i)
                for i, j in edges[::-1]:
                    if j == duplicate and (i in froms and froms[i]):
                        return [i, j]

        else:
            q = deque(end)
            while q:
                i = q.popleft()
                for nei in froms[i]:
                    graph[nei].remove(i)
                    if not graph[nei]:
                        q.append(nei)
                froms.pop(i)

            for i, j in edges[::-1]:
                if i in graph and j in graph[i]:
                    return (i, j)
        return []
