# 140. Word Break II
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i, cur):
            if i == n:
                res.append(" ".join(cur))
                return

            for j in range(i + 1, n + 1):
                if s[i:j] in words:
                    dfs(j, cur + [s[i:j]])

        words = set(wordDict)
        n = len(s)
        res = []
        dfs(0, [])
        return res
