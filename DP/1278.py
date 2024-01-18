# 1278. Palindrome Partitioning III
from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def cost(i, j):
            if i >= j:
                return 0
            return (s[i] != s[j - 1]) + cost(i + 1, j - 1)

        @cache
        def dp(i, k):
            if k == n - i:
                return 0
            if k == 1:
                return cost(i, n)

            costs = float("inf")
            for j in range(i + 1, n - k + 2):
                costs = min(costs, cost(i, j) + dp(j, k - 1))
            return costs

        return dp(0, k)


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def cost(w):
            length = len(w)
            if length == 1:
                return 0
            l, r = 0, length - 1
            cost = 0
            while l < r:
                if w[l] != w[r]:
                    cost += 1
                l += 1
                r -= 1
            return cost

        @cache
        def dp(i, k):
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return float("inf")

            costs = float("inf")
            for j in range(i + 1, n + 1):
                costs = min(costs, cost(s[i:j]) + dp(j, k - 1))
            return costs

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
