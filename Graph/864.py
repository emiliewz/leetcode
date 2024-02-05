# 864. Shortest Path to Get All Keys
from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    k += 1
                elif grid[i][j] == "@":
                    sx, sy = i, j
        complete = (1 << k) - 1
        q = deque([(0, sx, sy)])
        visit, steps = set((0, sx, sy)), 0
        keys = set()

        while q:
            for _ in range(len(q)):
                mask, x, y = q.popleft()
                if mask == complete:
                    return steps
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and grid[i][j] != "#":
                        cur = grid[i][j]
                        if cur.islower():
                            new_mask = mask | (1 << ord(cur) - ord("a"))
                            if (new_mask, i, j) not in visit:
                                visit.add((new_mask, i, j))
                                q.append((new_mask, i, j))
                                keys.add(cur)
                        else:
                            if cur in ".@" or (
                                cur.isupper()
                                and (mask & (1 << ord(cur.lower()) - ord("a")))
                            ):
                                if (mask, i, j) not in visit:
                                    q.append((mask, i, j))
                                    visit.add((mask, i, j))

            steps += 1
        return -1


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = [1 for i in range(m) for j in range(n) if grid[i][j].islower()]
        x, y = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "@")
        q = deque([(0, x, y)])
        visit = set((0, x, y))
        complete = (1 << len(keys)) - 1
        steps = 0

        while q:
            for _ in range(len(q)):
                mask, x, y = q.popleft()
                if mask == complete:
                    return steps

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and grid[i][j] != "#":
                        if grid[i][j].islower():
                            key = ord(grid[i][j]) - ord("a")
                            new_mask = mask | 1 << key
                            if (new_mask, i, j) not in visit:
                                visit.add((new_mask, i, j))
                                q.append((new_mask, i, j))
                        elif (mask, i, j) not in visit:
                            if grid[i][j] in ".@" or (
                                grid[i][j].isupper()
                                and mask & (1 << ord(grid[i][j]) - ord("A"))
                            ):
                                visit.add((mask, i, j))
                                q.append((mask, i, j))
            steps += 1

        return -1


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = [1 for i in range(m) for j in range(n) if grid[i][j].islower()]
        player = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "@")
        q = deque([(0, player)])
        visit = set((0, player))
        complete = (1 << len(keys)) - 1
        steps = 0

        while q:
            for _ in range(len(q)):
                mask, (x, y) = q.popleft()
                if mask == complete:
                    return steps

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and grid[i][j] != "#":
                        if grid[i][j].islower():
                            key = ord(grid[i][j]) - ord("a")
                            new_mask = mask | 1 << key
                            if (new_mask, (i, j)) not in visit:
                                visit.add((new_mask, (i, j)))
                                q.append((new_mask, (i, j)))
                        elif (mask, (i, j)) not in visit:
                            haveKey = True
                            if grid[i][j].isupper():
                                haveKey = mask & (1 << ord(grid[i][j]) - ord("A"))
                            if haveKey:
                                visit.add((mask, (i, j)))
                                q.append((mask, (i, j)))

            steps += 1

        return -1
