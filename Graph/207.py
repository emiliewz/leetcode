# 207. Course Schedule
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        froms = defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)
            froms[j].append(i)

        ends = [i for i in graph if not graph[i]]
        q = deque(ends)
        while q:
            cur = q.popleft()
            for i in froms[cur]:
                graph[i].remove(cur)
                if not graph[i]:
                    q.append(i)
            graph.pop(cur)

        return not graph


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preCrsNeed = {i: set() for i in range(numCourses)}
        crsCanDo = defaultdict(set)

        for c, p in prerequisites:
            preCrsNeed[c].add(p)
            crsCanDo[p].add(c)

        q = deque([])
        for i in range(numCourses):
            if not preCrsNeed[i]:
                q.append(i)

        while q:
            i = q.popleft()
            for j in crsCanDo[i]:
                preCrsNeed[j].remove(i)
                if len(preCrsNeed[j]) == 0:
                    q.append(j)
            preCrsNeed.pop(i)
        return not preCrsNeed


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(crs):
            if not a[crs]:
                return True
            if crs in visit:
                return False

            visit.add(crs)
            for pre in a[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            a[crs] = []
            return True

        a = defaultdict(list)
        for crs, pre in prerequisites:
            a[crs].append(pre)
        visit = set()
        for crs in range(numCourses):
            if a[crs]:
                if not dfs(crs):
                    return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a = [[] for _ in range(numCourses)]
        need = [0] * numCourses

        for crs, pre in prerequisites:
            a[pre].append(crs)
            need[crs] += 1

        bfs = [i for i in range(numCourses) if need[i] == 0]

        for pre in bfs:
            for crs in a[pre]:
                need[crs] -= 1
                if need[crs] == 0:
                    bfs.append(crs)

        return len(bfs) == numCourses
