# 409. Longest Palindrome
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set()
        n = len(s)
        for c in s:
            a ^= {c}

        return n - len(a) + 1 if a else n


class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = defaultdict(int)
        for c in s:
            a[c] += 1
        res = 0
        for _, j in a.items():
            res += j // 2

        return res * 2 + 1 if res * 2 != len(s) else res * 2
