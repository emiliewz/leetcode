# 131. Palindrome Partitioning
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(idx, cur):
            if idx == len(s):
                res.append(cur.copy())
                return
            for i in range(idx, len(s)):
                if s[idx : i + 1] == s[idx : i + 1][::-1]:
                    backtrack(i + 1, cur + [s[idx : i + 1]])

        backtrack(0, [])
        return res
