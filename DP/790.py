# 790. Domino and Tromino Tiling
from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        prev_empty, part, full = 0, 0, 1

        for i in range(n):
            tmp = full
            full = part * 2 + prev_empty + full
            part = prev_empty + part
            prev_empty = tmp

        return full % (10**9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        prev_full, full, part = 1, 2, 1

        for i in range(2, n):
            cur = full
            full += part * 2 + prev_full
            part += prev_full
            prev_full = cur

        return full % (10**9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        prev_full = 1
        cur_full = 2
        cur_top_empty = 1
        cur_bottom_empty = 1

        for i in range(2, n):
            a, b, c, d = prev_full, cur_full, cur_top_empty, cur_bottom_empty
            cur_full = a + b + c + d
            cur_top_empty = a + d
            cur_bottom_empty = a + c
            prev_full = b

        return cur_full % (10**9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        prev_full, full, part_fill = 1, 1, 0
        for i in range(1, n):
            tmp = full
            full += 2 * part_fill + prev_full
            part_fill += prev_full
            prev_full = tmp

        return full % (10**9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [[0] * n for _ in range(3)]
        dp[0][0] = 1
        dp[0][1] = 2
        dp[1][1] = 1
        dp[2][1] = 1

        for i in range(2, n):
            dp[0][i] = dp[2][i - 1] + dp[1][i - 1] + dp[0][i - 1] + dp[0][i - 2]
            dp[1][i] = dp[2][i - 1] + dp[0][i - 2]
            dp[2][i] = dp[1][i - 1] + dp[0][i - 2]

        return dp[0][-1] % (10**9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 2, 5] + [0] * n

        for i in range(3, n):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]

        return dp[n - 1] % (10**9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def dp(t, b):
            if t > n or b > n:
                return 0
            if t == b == n:
                return 1
            if t > b:
                return dp(t + 1, b + 2) + dp(t, b + 2)
            if t < b:
                return dp(t + 2, b) + dp(t + 2, b + 1)
            return (
                dp(t + 1, b + 1)
                + dp(t + 2, b + 1)
                + dp(t + 1, b + 2)
                + dp(t + 2, b + 2)
            )

        return dp(0, 0) % (10**9 + 7)
