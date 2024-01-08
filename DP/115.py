# 115. Distinct Subsequences
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
