# 1048. Longest String Chain
from typing import List


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
