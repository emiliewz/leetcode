# 980. Unique Paths III
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        zeros = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j
        res = 0

        def dp(i, j):
            nonlocal zeros, res
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                res += zeros == 0
                return

            grid[i][j] = -1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                zeros -= 1
                dp(i + dx, j + dy)
                zeros += 1
            grid[i][j] = 0

        dp(sx, sy)
        return res


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    empty += 1
        res = 0

        def dp(i, j, k):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                nonlocal res
                res += k == 0
                return

            grid[i][j] = -1
            dp(i + 1, j, k - 1)
            dp(i - 1, j, k - 1)
            dp(i, j + 1, k - 1)
            dp(i, j - 1, k - 1)
            grid[i][j] = 0

        dp(sx, sy, empty)
        return res


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sx, sy, count = 0, 0, 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    count += 1
        res = 0

        def dp(x, y, k):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                nonlocal res
                if k == 0:
                    res += 1
                return
            grid[x][y] = -1
            dp(x + 1, y, k - 1)
            dp(x - 1, y, k - 1)
            dp(x, y + 1, k - 1)
            dp(x, y - 1, k - 1)
            grid[x][y] = 0

        dp(sx, sy, count)
        return res


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sx, sy = 0, 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    count += 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        def dp(x, y, k):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                nonlocal res
                if k - 1 == count:
                    res += 1
                return
            grid[x][y] = -1
            for dx, dy in directions:
                dp(x + dx, y + dy, k + 1)
            # dp(x+1, y, k+1)
            # dp(x-1, y, k+1)
            # dp(x, y+1, k+1)
            # dp(x, y-1, k+1)
            grid[x][y] = 0

        dp(sx, sy, 0)
        return res
