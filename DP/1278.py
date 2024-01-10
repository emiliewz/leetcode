# 1278. Palindrome Partitioning III
from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def cost(i, j=len(s) - 1):
            return 0 if i >= j else cost(i + 1, j - 1) + (s[i] != s[j])

        @cache
        def dp(i, n):
            if n == 1:
                return cost(i)

            min_cost = float("inf")
            for j in range(i, len(s) - n + 1):
                min_cost = min(min_cost, cost(i, j) + dp(j + 1, n - 1))

            return min_cost

        return dp(0, k)


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def cost(i, j=len(s) - 1):
            return 0 if i >= j else cost(i + 1, j - 1) + (s[i] != s[j])

        @cache
        def dp(i, n):
            if n == 1:
                return cost(i)
            return min(
                (cost(i, j) + dp(j + 1, n - 1) for j in range(i, len(s) - n + 1)),
                default=0,
            )

        return dp(0, k)
