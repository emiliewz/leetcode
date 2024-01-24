# 695. Max Area of Island


from typing import List


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
