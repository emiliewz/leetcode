# 1048. Longest String Chain
from functools import cache
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        a = {}

        for w in words:
            a[w] = 1
            for j in range(len(w)):
                sub_word = w[:j] + w[j + 1 :]
                if sub_word in a:
                    a[w] = max(a[w], a[sub_word] + 1)
        return max(a.values())


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @cache
        def canChain(i, j):
            f, s = words[i], words[j]

            for k in range(length[j]):
                if f == s[:k] + s[k + 1 :]:
                    return True
            return False

        n = len(words)
        words.sort(key=len)
        length = [len(i) for i in words]
        a = [1] * n

        for i in range(1, n):
            for j in range(i):
                if length[j] < length[i] - 1 or length[i] == length[j]:
                    continue
                if canChain(j, i):
                    a[i] = max(a[j] + 1, a[i])
        return max(a)


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        a = {}
        for w in words:
            a[w] = 1
            for j in range(len(w)):
                if w[:j] + w[j + 1 :] in a:
                    a[w] = max(a[w], a[w[:j] + w[j + 1 :]] + 1)

        return max(a.values())


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_len = 0

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                pred_word = word[:i] + word[i + 1 :]
                if pred_word in dp:
                    dp[word] = max(dp[word], dp[pred_word] + 1)
            max_len = max(max_len, dp[word])

        return max_len
