# 943. Find the Shortest Superstring
from functools import cache
from itertools import permutations
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        complete = 1 << n

        @cache
        def connect(x, y):
            f, s = words[x], words[y]
            i = min(len(f), len(s))
            while i > 0:
                if f[-i:] == s[:i]:
                    return i
                i -= 1
            return 0

        a = [[(float("inf"), "")] * n for _ in range(complete)]
        for i in range(n):
            a[1 << i][i] = (len(words[i]), words[i])

        for mask in range(complete):
            words_in_bit = [i for i in range(n) if mask & (1 << i)]

            for i, j in permutations(words_in_bit, 2):
                new_word = a[mask ^ (1 << j)][i][1] + words[j][connect(i, j) :]
                if len(new_word) < a[mask][j][0]:
                    a[mask][j] = (len(new_word), new_word)

        return min(a[-1])[1]
