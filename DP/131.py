# 131. Palindrome Partitioning
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def backtrack(idx, cur):
            if idx == n:
                res.append(cur[:])
                return

            for i in range(idx, n):
                if s[idx : i + 1] == s[idx : i + 1][::-1]:
                    backtrack(i + 1, cur + [s[idx : i + 1]])

        backtrack(0, [])
        return res
