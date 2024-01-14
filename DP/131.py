# 131. Palindrome Partitioning
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 1:
            return [[s]]
        res = []

        def get_palindrome(i, cur):
            if i == n:
                res.append(cur)
                return
            for j in range(i + 1, n + 1):
                if s[i:j] == s[i:j][::-1]:
                    get_palindrome(j, cur + [s[i:j]])

        get_palindrome(0, [])
        return res


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
