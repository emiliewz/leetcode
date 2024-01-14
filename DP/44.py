# 44. Wildcard Matching
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        a = [[False] * (n + 1) for _ in range(m + 1)]
        a[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                a[0][j] = a[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    a[i][j] = a[i - 1][j - 1]
                elif p[j - 1] == "*":
                    a[i][j] = a[i][j - 1] or a[i - 1][j]

        return a[-1][-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dp(i, j):
            if j == n:
                return i == m
            if i == m:
                return p[j] == "*" and dp(i, j + 1)
            match = s[i] == p[j] or p[j] == "?"

            if p[j] == "*":
                return dp(i, j + 1) or dp(i + 1, j)
            if match:
                return dp(i + 1, j + 1)
            return False

        return dp(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dfs(i, j):
            if j == n:
                return i == m

            if (i, j) in memo:
                return memo[(i, j)]

            if i == m:
                memo[(i, j)] = p[j] == "*" and dfs(i, j + 1)
                return memo[(i, j)]

            if p[j] == "*":
                memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
                return memo[(i, j)]

            if p[j] == "?" or s[i] == p[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return False

        return dfs(0, 0)
