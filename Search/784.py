# 784. Letter Case Permutation
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur)
                return

            dfs(i + 1, cur + s[i])

            if s[i].isupper():
                dfs(i + 1, cur + s[i].lower())
            elif s[i].islower():
                dfs(i + 1, cur + s[i].upper())

        dfs(0, "")
        return res
