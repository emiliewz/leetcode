# 943. Find the Shortest Superstring
from functools import cache
from itertools import permutations
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @cache
        def connect(x, y):
            f, s = words[x], words[y]
            i = min(len(f), len(s))
            while i > 0:
                if f[-i:] == s[:i]:
                    return i
                i -= 1
            return 0

        n = len(words)
        complete = (1 << n) - 1
        a = [[(float("inf"), "")] * n for _ in range(complete + 1)]

        for i in range(n):
            a[1 << i][i] = (len(words[i]), words[i])

        for mask in range(1 << n):
            wordInBit = [i for i in range(n) if mask & (1 << i)]
            for f, s in permutations(wordInBit, 2):
                new_word = a[mask ^ (1 << s)][f][1] + words[s][connect(f, s) :]
                if len(new_word) < a[mask][s][0]:
                    a[mask][s] = (len(new_word), new_word)

        return min(a[-1])[1]


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        complete = 1 << n
        a = [[(float("inf"), "")] * n for _ in range(complete)]

        @cache
        def costs(j, k):
            i = min(len(words[j]), len(words[k]))
            while i >= 0:
                if words[j][-i:] == words[k][:i]:
                    return i
                i -= 1
            return 0

        for i in range(n):
            a[1 << i][i] = (len(words[i]), words[i])

        for i in range(complete):
            have_words = [j for j in range(n) if i & (1 << j)]
            for j, k in permutations(have_words, 2):
                pre_mask = i ^ (1 << k)
                new_words = a[pre_mask][j][1] + words[k][costs(j, k) :]
                if len(new_words) < a[i][k][0]:
                    a[i][k] = (len(new_words), new_words)
        return min(a[-1])[1]
