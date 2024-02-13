# 664. Strange Printer
from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        a = [[n] * n for _ in range(n)]
        for i in range(n):
            a[i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                cur = i + 1
                while cur < n and s[cur] == s[cur - 1]:
                    cur += 1
                a[i][j] = a[cur][j] + 1 if cur <= j else 1
                for k in range(cur, j + 1):
                    if s[k] == s[i]:
                        a[i][j] = min(a[i][j], a[cur][k - 1] + a[k][j])
        return a[0][n - 1]


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i, j):
            if i > j:
                return 0

            cur = i + 1
            while cur < n and s[cur] == s[cur - 1]:
                cur += 1

            res = dfs(cur, j) + 1

            for h in range(cur, j + 1):
                if s[h] == s[i]:
                    res = min(res, dfs(cur, h - 1) + dfs(h, j))
            return res

        return dfs(0, n - 1)
