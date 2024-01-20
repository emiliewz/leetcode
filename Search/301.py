# 301. Remove Invalid Parentheses
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            elif s[i] == ")":
                if l == 0:
                    r += 1
                else:
                    l -= 1

        def isValid(s):
            i = 0
            l, r = 0, 0
            while i < len(s):
                if s[i] == "(":
                    l += 1
                elif s[i] == ")":
                    r += 1
                    if r > l:
                        return False
                i += 1
            return l == r

        def dfs(idx, l, r, cur):
            if l == r == 0:
                if isValid(cur):
                    res.append(cur)
                return

            for i in range(idx, len(cur)):
                if i > idx and cur[i] == cur[i - 1]:
                    continue
                if cur[i] == "(" and l > 0:
                    dfs(i, l - 1, r, cur[:i] + cur[i + 1 :])
                elif cur[i] == ")" and r > 0:
                    dfs(i, l, r - 1, cur[:i] + cur[i + 1 :])

        res = []
        dfs(0, l, r, s)
        return res


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0

        for c in s:
            if c == "(":
                l += 1
            elif c == ")":
                if l == 0:
                    r += 1
                else:
                    l -= 1

        def isValid(str):
            l, r = 0, 0
            for c in str:
                if c == "(":
                    l += 1
                elif c == ")":
                    r += 1
                    if r > l:
                        return False
            return l == r

        def backtrack(idx, l, r, cur):
            if l == 0 and r == 0:
                if isValid(cur):
                    res.append(cur)
                    return

            for i in range(idx, len(cur)):
                if i > idx and cur[i] == cur[i - 1]:
                    continue
                if cur[i] == "(" and l > 0:
                    backtrack(i, l - 1, r, cur[:i] + cur[i + 1 :])
                elif cur[i] == ")" and r > 0:
                    backtrack(i, l, r - 1, cur[:i] + cur[i + 1 :])

        backtrack(0, l, r, s)
        return res
