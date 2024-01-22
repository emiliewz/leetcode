# 200. Number of Islands
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if (
                i < 0
                or i >= m
                or j < 0
                or j >= n
                or grid[i][j] == "0"
                or (i, j) in visit
            ):
                return
            visit.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    res += 1
        return res
