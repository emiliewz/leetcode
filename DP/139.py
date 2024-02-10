# 139. Word Break
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        a = [False] * (n + 1)
        a[0] = True
        words = set(wordDict)

        for i in range(n + 1):
            for j in range(i):
                if a[j] and s[j:i] in words:
                    a[i] = True
                    break

        return a[-1]
