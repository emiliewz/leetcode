# 664. Strange Printer
from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        a = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            a[i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                a[i][j] = 1 + a[i + 1][j]
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        a[i][j] = min(
                            a[i][j], a[i][k - 1] + (a[k + 1][j] if k < j else 0)
                        )

        return a[0][n - 1]


class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(l, r):
            if l > r:
                return 0

            res = 1 + dp(l + 1, r)
            for i in range(l + 1, r + 1):
                if s[i] == s[l]:
                    res = min(res, dp(l, i - 1) + dp(i + 1, r))
            return res

        return dp(0, len(s) - 1)


class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(l, r):
            if l > r:
                return 0

            min_count = dp(l + 1, r) + 1
            for i in range(l + 1, r + 1):
                if s[i] == s[l]:
                    min_count = min(min_count, dp(l + 1, i) + dp(i + 1, r))

            return min_count

        return dp(0, len(s) - 1)


class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(l, r):
            if l > r:
                return 0

            min_count = dp(l, r - 1) + 1

            for i in range(l, r):
                if s[i] == s[r]:
                    min_count = min(min_count, dp(l, i) + dp(i + 1, r - 1))

            return min_count

        return dp(0, len(s) - 1)
