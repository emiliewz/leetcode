# 131. Palindrome Partitioning
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i, cur):
            if i == n:
                res.append(cur)
                return

            for j in range(i + 1, n + 1):
                if s[i:j] == s[i:j][::-1]:
                    dfs(j, cur + [s[i:j]])

        n = len(s)
        res = []
        dfs(0, [])
        return res
