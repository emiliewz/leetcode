# 935. Knight Dialer
from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [
            (-1, -2),
            (-1, 2),
            (-2, -1),
            (-2, 1),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
        ]

        @cache
        def dp(x, y, k):
            if x < 0 or x >= 4 or y < 0 or y >= 3 or (x == 3 and not y == 1):
                return 0
            if k == n - 1:
                return 1
            res = 0
            for dx, dy in directions:
                res += dp(x + dx, y + dy, k + 1)
            return res

        res = 0
        for i in range(4):
            for j in range(3):
                res += dp(i, j, 0)
                res %= 10**9 + 7

        return res


class Solution:
    def knightDialer(self, n: int) -> int:
        memo = {}

        directions = [
            (-1, -2),
            (-1, 2),
            (-2, -1),
            (-2, 1),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
        ]

        def dp(x, y, k):
            if (x, y, k) in memo:
                return memo[(x, y, k)]
            if x < 0 or x >= 4 or y < 0 or y >= 3 or (x == 3 and not y == 1):
                return 0
            if k == n - 1:
                return 1

            res = 0
            for dx, dy in directions:
                res += dp(x + dx, y + dy, k + 1)

            memo[(x, y, k)] = res
            return res

        res = 0
        for i in range(4):
            for j in range(3):
                res += dp(i, j, 0)

        return res % (10**9 + 7)
