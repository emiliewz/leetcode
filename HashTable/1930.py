# 1930. Unique Length-3 Palindromic Subsequences
from string import ascii_lowercase


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in ascii_lowercase:
            l, h = s.find(c), s.rfind(c)
            if l > -1:
                res += len(set(s[l + 1 : h]))
        return res
