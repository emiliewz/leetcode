# 827. Making A Large Island
from collections import Counter, deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(i, j):
            p1, p2 = find(i), find(j)
            p[p1] = p2

        n = len(grid)
        a, k, candidates = {}, 0, set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    a[i, j] = k
                    k += 1
                else:
                    candidates.add((i, j))
        if not k:
            return 1
        if k == n**2:
            return n**2
        p = list(range(k))
        for i, j in a:
            if (i - 1, j) in a:
                union(a[i, j], a[i - 1, j])
            if (i, j - 1) in a:
                union(a[i, j], a[i, j - 1])
        islands = dict(Counter([find(i) for i in range(k)]))
        res = 0
        for x, y in candidates:
            canConnect = set()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                i, j = x + dx, y + dy
                if (i, j) in a:
                    canConnect.add(find(a[i, j]))
            res = max(res, sum([islands[i] for i in canConnect]) + 1)
        return res


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(k):
            q, move = deque(lands[k]), 0
            visit = set(lands[k])
            nei_area = 0

            while q and move < 2:
                for _ in range(len(q)):
                    cx, cy = q.popleft()
                    cur = 0
                    nei = set()

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = cx + dx, cy + dy

                        if (0 <= nx < n) and (0 <= ny < n):
                            if (nx, ny) not in visit:
                                visit.add((nx, ny))
                                q.append((nx, ny))

                            if grid[nx][ny] not in [0, k]:
                                nei.add(grid[nx][ny])
                    cur += sum(lands_size[i] for i in nei)
                    nei_area = max(cur, nei_area)
                move += 1
            return nei_area

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] in [0, k]:
                return 0
            grid[i][j] = k
            lands.setdefault(k, []).append((i, j))
            area = 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return area

        n = len(grid)
        lands, k = {}, 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    k += 1
        max_area = 0
        if not lands:
            return 1
        lands_size = {i: len(lands[i]) for i in lands}

        for i in lands:
            area = lands_size[i] + 1
            max_area = max(max_area, area + bfs(i))

        return min(max_area, n**2)
