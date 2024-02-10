# 1048. Longest String Chain
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
