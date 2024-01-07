# 97. Interleaving String
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)

        if m + n != l:
            return False

        if m < n:
            return self.isInterleave(s2, s1, s3)

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )
        return dp[n]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[m][n]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        memo = {}

        def dfs(i, j, k, m, n):
            if k == l3:
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            if i == l1:
                return s2[j:] == s3[k:]
            if j == l2:
                return s1[i:] == s3[k:]

            if s1[i] == s2[j] == s3[k]:
                memo[(i, j)] = dfs(i + 1, j, k + 1, m + 1, n) or dfs(
                    i, j + 1, k + 1, m, n + 1
                )
                return memo[(i, j)]
            if s1[i] == s3[k]:
                memo[(i, j)] = dfs(i + 1, j, k + 1, m + 1, n)
                return memo[(i, j)]
            if s2[j] == s3[k]:
                memo[(i, j)] = dfs(i, j + 1, k + 1, m, n + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return False

        return dfs(0, 0, 0, 0, 0)
