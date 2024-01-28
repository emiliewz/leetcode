# 1263. Minimum Moves to Move a Box to Their Target Location
from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        box = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "B")
        player = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "S")
        target = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "T")

        def valid(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "#":
                return False
            return True

        h = [(0, player, box)]
        visit = set((player, box))

        while h:
            k, p, b = heappop(h)
            if b == target:
                return k

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_p = (p[0] + dx, p[1] + dy)
                if new_p == b:
                    new_b = (p[0] + 2 * dx, p[1] + 2 * dy)
                    if (new_p, new_b) not in visit and valid(*new_b):
                        visit.add((new_p, new_b))
                        heappush(h, (k + 1, new_p, new_b))
                elif (new_p, b) not in visit and valid(*new_p):
                    visit.add((new_p, b))
                    heappush(h, (k, new_p, b))

        return -1


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        box = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "B")
        player = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "S")
        target = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "T")
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != "#"

        def canArrive(beginPos, endPos, boxPos):
            q = deque([beginPos])
            visit = set(beginPos)
            while q:
                cx, cy = q.popleft()
                if (cx, cy) == endPos:
                    return True
                for dx, dy in directions:
                    new_pos = (cx + dx, cy + dy)
                    if valid(*new_pos) and new_pos not in visit and new_pos != boxPos:
                        visit.add(new_pos)
                        q.append(new_pos)
            return False

        q = deque([(0, box, player)])
        visit = set((box, player))

        while q:
            k, b, p = q.popleft()
            if b == target:
                return k

            for dx, dy in directions:
                new_b = b[0] + dx, b[1] + dy
                new_p = b[0] - dx, b[1] - dy
                if valid(*new_b) and valid(*new_p):
                    if canArrive(p, new_p, b) and (new_b, new_p) not in visit:
                        visit.add((new_b, new_p))
                        q.append((k + 1, new_b, new_p))

        return -1
