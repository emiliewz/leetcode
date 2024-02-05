# 1129. Shortest Path with Alternating Colors
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        a = {i: {0: [], 1: []} for i in range(n)}
        for i, j in redEdges:
            a[i][0].append(j)
        for i, j in blueEdges:
            a[i][1].append(j)

        res = [-1] * n
        q = deque([(0, 1), (0, 0)])
        visit = set()
        steps = 0
        while q:
            for _ in range(len(q)):
                cur, color = q.popleft()
                visit.add((cur, color))
                if res[cur] == -1:
                    res[cur] = steps
                new_color = color ^ 1
                for nei in a[cur][new_color]:
                    if (nei, new_color) not in visit:
                        q.append((nei, new_color))
            steps += 1

        return res


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        def bfs(i):
            q = deque([(0, 1), (0, 0)])
            visit, steps = set(), 0
            while q:
                for _ in range(len(q)):
                    cur, color = q.popleft()
                    visit.add((cur, color))
                    if cur == i:
                        return steps
                    if color == 0:
                        for nei in blue[cur]:
                            if (nei, 1) not in visit:
                                q.append((nei, 1))
                    if color == 1:
                        for nei in red[cur]:
                            if (nei, 0) not in visit:
                                q.append((nei, 0))
                steps += 1
            return -1

        red = defaultdict(list)
        blue = defaultdict(list)
        for i, j in redEdges:
            red[i].append(j)
        for i, j in blueEdges:
            blue[i].append(j)
        res = [0] * n

        for i in range(1, n):
            res[i] = bfs(i)

        return res


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        a = defaultdict(dict)
        for i, j in redEdges:
            a[j].setdefault(0, []).append(i)
        for i, j in blueEdges:
            a[j].setdefault(1, []).append(i)

        def bfs(idx):
            moves = 0
            q = deque([(idx, 0), (idx, 1)])
            visit = set()
            visit.add((idx, 1))
            visit.add((idx, 0))

            while q:
                for _ in range(len(q)):
                    i, c = q.popleft()
                    if i == 0:
                        return moves
                    color = c ^ 1

                    if color in a[i]:
                        for nei in a[i][color]:
                            if (nei, color) not in visit:
                                visit.add((nei, color))
                                q.append((nei, color))
                moves += 1
            return -1

        res = [-1] * n
        res[0] = 0

        for i in range(1, n):
            if i in a:
                res[i] = bfs(i)

        return res
