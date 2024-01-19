# 741. Cherry Pickup
from functools import cache
from typing import List


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
                        a[r1][c1 + 1][r2 + 1]
                        if c1 < n - 1 and r2 < n - 1
                        else -float("inf"),
                        a[r1 + 1][c1][r2] if r1 < n - 1 else -float("inf"),
                        a[r1 + 1][c1][r2 + 1]
                        if r1 < n - 1 and r2 < n - 1
                        else -float("inf"),
                    )

        return max(0, a[0][0][0])


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0
        n = len(grid)

        @cache
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if (
                r1 >= n
                or c1 >= n
                or r2 >= n
                or c2 >= n
                or grid[r1][c1] == -1
                or grid[r2][c2] == -1
            ):
                return -float("inf")

            if r1 == c1 == n - 1:
                return grid[-1][-1]

            cur_cherry = grid[r1][c1] if (r1 == r2) else grid[r1][c1] + grid[r2][c2]

            return cur_cherry + max(
                dp(r1, c1 + 1, r2),
                dp(r1, c1 + 1, r2 + 1),
                dp(r1 + 1, c1, r2),
                dp(r1 + 1, c1, r2 + 1),
            )

        return max(dp(0, 0, 0), 0)


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def dp(r1, c1, r2, c2):
            if (
                r1 >= n
                or c1 >= n
                or r2 >= n
                or c2 >= n
                or grid[r1][c1] < 0
                or grid[r2][c2] < 0
            ):
                return -float("inf")

            if r1 == c1 == n - 1:
                return grid[r1][c1]

            cur_cherry = (
                grid[r1][c1] if r1 == r2 and c1 == c2 else grid[r1][c1] + grid[r2][c2]
            )

            next_cherry = -float("inf")

            for i in directions:
                for j in directions:
                    next_cherry = max(
                        next_cherry, dp(r1 + i[0], c1 + i[1], r2 + j[0], c2 + j[1])
                    )

            return cur_cherry + next_cherry

        if grid[0][0] < 0 or grid[-1][-1] < 0:
            return 0
        directions = [(0, 1), (1, 0)]
        n = len(grid)
        res = dp(0, 0, 0, 0)
        return res if res != -float("inf") else 0
