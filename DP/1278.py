# 1278. Palindrome Partitioning III
from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def get_cost(i, j=n):
            if j <= i + 1:
                return 0
            return (s[i] != s[j - 1]) + get_cost(i + 1, j - 1)

        @cache
        def dfs(i, k):
            if k == n - i:
                return 0

            if k == 1:
                return get_cost(i)

            res = float("inf")
            for j in range(i + 1, n):
                cur_cost = get_cost(i, j)
                res = min(cur_cost + dfs(j, k - 1), res)
            return res

        return dfs(0, k)
