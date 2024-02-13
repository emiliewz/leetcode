# 741. Cherry Pickup
from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0

        @cache
        def dfs(x1, y1, x2):
            y2 = x1 + y1 - x2
            if (
                x1 >= n
                or y1 >= n
                or grid[x1][y1] == -1
                or x2 >= n
                or y2 >= n
                or grid[x2][y2] == -1
            ):
                return -float("inf")
            if x1 == y1 == n - 1:
                return grid[x1][y1]

            next_cherry = -float("inf")
            cur_cherry = grid[x1][y1] + grid[x2][y2]

            if x1 == x2 and y1 == y2:
                cur_cherry -= grid[x1][y1]

            return cur_cherry + max(
                next_cherry,
                dfs(x1 + 1, y1, x2 + 1),
                dfs(x1, y1 + 1, x2),
                dfs(x1 + 1, y1, x2),
                dfs(x1, y1 + 1, x2 + 1),
            )

        return max(dfs(0, 0, 0), 0)


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0
        n = len(grid)
        a = [[[-float("inf")] * n for _ in range(n)] for _1 in range(n)]

        for r1 in range(n - 1, -1, -1):
            for c1 in range(n - 1, -1, -1):
                for r2 in range(n - 1, -1, -1):
                    c2 = (r1 + c1) - r2
                    if c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    if r1 == n - 1 == c1:
                        a[r1][c1][r2] = grid[-1][-1]
                        continue
                    cur_cherry = (
                        grid[r1][c1] if r1 == r2 else grid[r1][c1] + grid[r2][c2]
                    )

                    a[r1][c1][r2] = cur_cherry + max(
                        a[r1][c1 + 1][r2] if c1 < n - 1 else -float("inf"),
                        (
                            a[r1][c1 + 1][r2 + 1]
                            if c1 < n - 1 and r2 < n - 1
                            else -float("inf")
                        ),
                        a[r1 + 1][c1][r2] if r1 < n - 1 else -float("inf"),
                        (
                            a[r1 + 1][c1][r2 + 1]
                            if r1 < n - 1 and r2 < n - 1
                            else -float("inf")
                        ),
                    )

        return max(0, a[0][0][0])
