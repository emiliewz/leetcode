# 664. Strange Printer
from functools import cache


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
