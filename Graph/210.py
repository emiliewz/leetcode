# 210. Course Schedule II
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        froms = defaultdict(list)

        for i, j in prerequisites:
            graph[i].append(j)
            froms[j].append(i)

        ends = [i for i in graph if not graph[i]]
        q = deque(ends)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)

            for i in froms[cur]:
                graph[i].remove(cur)
                if not graph[i]:
                    q.append(i)
            graph.pop(cur)

        return res if not graph else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        todo = []
        preq = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)

        for i, j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)

        q = deque([k for k, v in preq.items() if not v])

        while q:
            course = q.popleft()
            todo.append(course)
            for c in graph[course]:
                preq[c].remove(course)
                if not preq[c]:
                    q.append(c)
            preq.pop(course)

        return todo if not preq else []
