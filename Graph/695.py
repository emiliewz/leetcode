# 695. Max Area of Island
from collections import Counter
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(i, j):
            p1, p2 = find(i), find(j)
            p[p1] = p2

        m, n = len(grid), len(grid[0])
        a = {}
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    a[i, j] = k
                    k += 1
        if not k:
            return 0
        p = list(range(k))
        for i, j in a:
            if (i - 1, j) in a:
                union(a[i - 1, j], a[i, j])
            if (i, j - 1) in a:
                union(a[i, j - 1], a[i, j])
        res = Counter([find(i) for i in range(k)]).most_common()[0][1]
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            nonlocal cur_area
            if x < 0 or x >= m or y < 0 or y >= n or not grid[x][y]:
                return
            cur_area += 1
            grid[x][y] = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(x + dx, y + dy)

        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cur_area = 0
                    dfs(i, j)
                    max_area = max(cur_area, max_area)
        return max_area
