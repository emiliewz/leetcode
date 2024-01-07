# 44. Wildcard Matching
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
