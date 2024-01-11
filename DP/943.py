# 943. Find the Shortest Superstring
from functools import cache
from typing import List


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
