# 943. Find the Shortest Superstring
from functools import cache
from itertools import permutations
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @cache
        def connect(f, s):
            i, l = 1, 0
            while i <= min(len(f), len(s)):
                if f[-i:] == s[:i]:
                    l = i
                i += 1
            return s[l:]

        n = len(words)
        end = 1 << n
        a = [[(float("inf"), "")] * n for _ in range(end)]

        for i in range(n):
            a[1 << i][i] = (len(words[i]), words[i])

        for mask in range(end):
            have_words_bits = [i for i in range(n) if mask & (1 << i)]

            for f, s in permutations(have_words_bits, 2):
                new_words = a[mask ^ (1 << s)][f][1] + connect(words[f], words[s])
                a[mask][s] = min(a[mask][s], (len(new_words), new_words))

        return min(a[-1])[1]


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @cache
        def connect(f, s):
            l, i = 0, 1
            while i <= min(len(f), len(s)):
                if f[len(f) - i :] == s[:i]:
                    l = i
                i += 1
            return s[l:]
            # return [s[i:] for i in range(len(f) + 1) if f[-i:] == s[:i] or not i][-1]

        n = len(words)
        dp = [[(float("inf"), "")] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = (len(words[i]), words[i])

        for mask in range(1 << n):
            n_z_bits = [j for j in range(n) if mask & 1 << j]

            for f, s in permutations(n_z_bits, 2):
                new_word = dp[mask ^ 1 << s][f][1] + connect(words[f], words[s])
                dp[mask][s] = min(dp[mask][s], (len(new_word), new_word))

        return min(dp[-1])[1]


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        origin = "".join(words)
        res = [origin]

        def backtrack(words, cur, size):
            if not words and len(cur) < len(res[-1]):
                res.append(cur)
                # print(res)
                return
            for i in range(len(words)):
                l = findOverlap(cur, words[i])
                if l >= size:
                    newStr = words[i] if cur == "" else words[i][l:]
                    # print('curStr: ', cur, ' and words[i]: ', words[i], ' overlap: ', newStr)
                    backtrack(words[:i] + words[i + 1 :], cur + newStr, size)

        @cache
        def findOverlap(f, s):
            l, i = 0, 1
            while i <= min(len(f), len(s)):
                if f[len(f) - i :] == s[:i]:
                    l = i
                i += 1
            # return s[l:]
            return l
            # return [s[i:] for i in range(len(f) + 1) if f[-i:] == s[:i] or not i][-1]

        backtrack(words, "", 0)
        return res[-1]
