# 10. Regular Expression Matching
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
