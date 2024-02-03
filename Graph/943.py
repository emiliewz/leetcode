# 943. Find the Shortest Superstring
from functools import cache
from itertools import permutations
from typing import List


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
