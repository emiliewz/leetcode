# 1129. Shortest Path with Alternating Colors
from collections import defaultdict, deque
from typing import List


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
