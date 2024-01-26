# 210. Course Schedule II
from collections import defaultdict, deque
from typing import List


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
