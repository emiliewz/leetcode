# 139. Word Break
from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(i):
            if i == n:
                return True

            for j in range(i + 1, n + 1):
                if s[i:j] in words:
                    if dfs(j):
                        return True
            return False

        n = len(s)
        words = set(wordDict)
        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        a = [False] * (n + 1)
        a[0] = True

        for i in range(n + 1):
            for j in range(i):
                if a[j] and s[j:i] in wordDict:
                    a[i] = True
                    break

        return a[n]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return True

            for j in range(i, n + 1):
                if s[i:j] in wordDict:
                    if dfs(j):
                        return True
            return False

        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        find = [False] * (n + 1)
        find[0] = True
        words = set(wordDict)

        for i in range(n + 1):
            for j in range(i):
                if find[j] and s[j:i] in words:
                    find[i] = True
                    break

        return find[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True

            for j in range(i, len(s) + 1):
                if s[i:j] in words:
                    if dfs(j):
                        return True
            return False

        return dfs(0)
