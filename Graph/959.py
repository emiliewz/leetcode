# 959. Regions Cut By Slashes
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 != p2:
                p[p1] = p2

        n = len(grid)
        p = list(range(4 * n * n))
        for i in range(n):
            for j in range(n):
                cur = (i * n + j) * 4
                if grid[i][j] != "/":
                    union(cur + 0, cur + 3)
                    union(cur + 1, cur + 2)
                if grid[i][j] != "\\":
                    union(cur + 0, cur + 1)
                    union(cur + 2, cur + 3)
                if i > 0:
                    top = ((i - 1) * n + j) * 4
                    union(cur + 0, top + 2)
                if j > 0:
                    left = (i * n + (j - 1)) * 4
                    union(cur + 1, left + 3)

        res = [find(i) for i in range(4 * n * n)]
        return len(set(res))


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 != p2:
                p[p1] = p2

        n = len(grid)
        p = list(range(4 * n**2))

        for i in range(n):
            for j in range(n):
                print("grid", grid[i][j])
                cur = (i * n + j) * 4
                pre_r = ((i - 1) * n + j) * 4
                pre_c = (i * n + j - 1) * 4
                if i:
                    union(pre_r + 2, cur + 0)
                if j:
                    union(pre_c + 1, cur + 3)
                if grid[i][j] != "/":
                    union(cur + 0, cur + 1)
                    union(cur + 2, cur + 3)
                if grid[i][j] != "\\":
                    union(cur + 0, cur + 3)
                    union(cur + 1, cur + 2)
        return len(set([find(i) for i in range(4 * n**2)]))
