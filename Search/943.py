# 943. Find the Shortest Superstring

from functools import cache
from itertools import permutations
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @cache
        def connect(f, s):
            m = min(len(f), len(s))
            l, i = 0, 1

            while i <= m:
                if f[-i:] == s[:i]:
                    l = i
                i += 1
            return s[l:]

        n = len(words)
        a = [[(float("inf"), "")] * n for _ in range(1 << n)]

        for i in range(n):
            a[1 << i][i] = (len(words[i]), words[i])

        for i in range(1 << n):
            word_bits = [j for j in range(n) if i & 1 << j]
            for f, s in permutations(word_bits, 2):
                new_word = a[i ^ 1 << s][f][1] + connect(words[f], words[s])
                a[i][s] = min(a[i][s], (len(new_word), new_word))

        return min(a[-1])[1]


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        origin = "".join(words)
        res = [origin]

        def backtrack(words, cur):
            if not words and len(cur) < len(res[-1]):
                res.append(cur)
                # print(res)
                return
            for i in range(len(words)):
                newStr = words[i] if cur == "" else findOverlap(cur, words[i])
                # print('curStr: ', cur, ' and words[i]: ', words[i], ' overlap: ', newStr)
                backtrack(words[:i] + words[i + 1 :], cur + newStr)

        def findOverlap(f, s):
            l, i = 0, 1
            while i <= min(len(f), len(s)):
                if f[len(f) - i :] == s[:i]:
                    l = i
                i += 1
            return s[l:]
            # return [s[i:] for i in range(len(f) + 1) if f[-i:] == s[:i] or not i][-1]

        backtrack(words, "")
        return res[-1]
