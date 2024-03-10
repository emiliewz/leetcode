# 409. Longest Palindrome
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        return min(sum(i // 2 * 2 for i in count.values()) + 1, len(s))
