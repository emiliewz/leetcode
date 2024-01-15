# 115. Distinct Subsequences
from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        a = [1] + [0] * n

        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    a[j] += tmp[j - 1]

        return a[-1]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        a = [1] + [0] * n

        for i in range(1, m + 1):
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    a[j] += a[j - 1]

        return a[-1]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        a = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            a[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a[i][j] = a[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    a[i][j] += a[i - 1][j - 1]

        return a[-1][-1]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        if m == n:
            return 1 if s == t else 0

        @cache
        def dp(i, j):
            if j == n:
                return 1

            if i == m:
                return 1 if j == t else 0

            if s[i] == t[j]:
                return dp(i + 1, j) + dp(i + 1, j + 1)
            else:
                return dp(i + 1, j)

        return dp(0, 0)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # skip current char
                dp[i][j] = dp[i - 1][j]
                if s[i] == t[j]:
                    # take this character
                    dp[i][j] += dp[i - 1][j - 1]

        return


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = {}

        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            not_take = dfs(i + 1, j)
            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)

            memo[(i, j)] = not_take + take
            return not_take + take

        return dfs(0, 0)
