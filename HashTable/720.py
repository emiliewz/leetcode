# 720. Longest Word in Dictionary
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        if len(words[0]) > 1:
            return ""
        max_len, a, res = 0, set(), []
        for word in words:
            n = len(word)
            if n == 1 or word[:-1] in a:
                a.add(word)
                if n > max_len:
                    max_len = n
                    res = [word]
                elif n == max_len:
                    res.append(word)
        return res[0] if len(res) == 1 else min(res)
