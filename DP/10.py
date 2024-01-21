# 10. Regular Expression Matching
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        a = [[False] * (n + 1) for _ in range(m + 1)]
        a[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == "*":
                a[0][i] = a[0][i - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match = p[j - 1] in [".", s[i - 1]]
                if p[j - 1] == "*":
                    a[i][j] = a[i][j - 2] or (
                        a[i - 1][j] and p[j - 2] in [".", s[i - 1]]
                    )
                if match:
                    a[i][j] = a[i - 1][j - 1]
        return a[-1][-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        a = [[False] * (n + 1) for _ in range(m + 1)]
        a[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                a[0][j] = a[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "." or s[i - 1] == p[j - 1]:
                    a[i][j] = a[i - 1][j - 1]
                elif p[j - 1] == "*":
                    a[i][j] = a[i][j - 2] or (
                        p[j - 2] == "." or s[i - 1] == p[j - 2] and a[i - 1][j]
                    )

        return a[-1][-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dp(i, j):
            if j == n:
                return i == m
            if i == m:
                return j + 1 < n and p[j + 1] == "*" and dp(i, j + 2)

            match = p[j] == "." or p[j] == s[i]

            if j + 1 < n and p[j + 1] == "*":
                return dp(i, j + 2) or (match and dp(i + 1, j))
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
                memo[(i, j)] = j + 1 < n and p[j + 1] == "*" and dfs(i, j + 2)
                return memo[(i, j)]

            match = p[j] == "." or p[j] == s[i]
            if j + 1 < n and p[j + 1] == "*":
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False

        return dfs(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m and j == n:
                return True
            if j == n:
                return False

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if j + 1 < n and p[j + 1] == "*":
                memo[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False

        return dfs(0, 0)
