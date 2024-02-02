# 847. Shortest Path Visiting All Nodes
from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = deque([])
        n = len(graph)
        seen = set()

        for i in range(n):
            q.append((i, 1 << i))
            seen.add((i, 1 << i))

        steps = 0
        complete = (1 << n) - 1

        while q:
            for _ in range(len(q)):
                cur, seen_state = q.popleft()
                if seen_state == complete:
                    return steps

                for i in graph[cur]:
                    new_state = seen_state | (1 << i)
                    if (i, new_state) not in seen:
                        seen.add((i, new_state))
                        q.append((i, new_state))

            steps += 1

        return -1
