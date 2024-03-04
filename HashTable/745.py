# 745. Prefix and Suffix Search
from collections import defaultdict
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.pref = defaultdict(set)
        self.suff = defaultdict(set)
        self.words = words
        self.a = set()
        n = len(words)
        for i, word in enumerate(words[::-1]):
            if word in self.a:
                continue
            self.a.add(word)
            self.pref[word[0]].add(n - i - 1)
            self.suff[word[-1]].add(n - i - 1)

    def f(self, pref: str, suff: str) -> int:
        p, s = pref[0], suff[-1]
        if p not in self.pref or s not in self.suff:
            return -1
        candidates = self.pref[p] & self.suff[s]
        for i in sorted(candidates, reverse=True):
            word = self.words[i]
            if word.startswith(pref) and word.endswith(suff):
                return i

        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
