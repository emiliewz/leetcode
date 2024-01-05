# 943. Find the Shortest Superstring

from typing import List


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
