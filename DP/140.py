# 140. Word Break II
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []

        def dp(i, cur):
            if i == n:
                res.append(" ".join(cur))
                return

            for j in range(i, n + 1):
                if s[i:j] in wordDict:
                    dp(j, cur + [s[i:j]])

        dp(0, [])
        return res


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)

        def dfs(idx, cur):
            if idx == n:
                res.append(" ".join(cur))
                return

            for i in range(idx, n + 1):
                if s[idx:i] in words:
                    dfs(i, cur + [s[idx:i]])

        res = []
        dfs(0, [])
        return res
