# 748. Shortest Completing Word
from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=len)
        a = Counter(i for i in licensePlate.lower() if i.isalpha())
        l = len(a)
        for word in words:
            n = len(word)
            if n < l:
                continue
            if Counter(word) >= a:
                return word
        return ""
