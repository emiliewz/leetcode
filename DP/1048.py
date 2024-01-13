# 1048. Longest String Chain
from typing import List


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
