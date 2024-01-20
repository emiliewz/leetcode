# 22. Generate Parentheses
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, cur):
            if l < r or l > n or r > n:
                return
            if l == r == n:
                res.append(cur)
                return 1

            dfs(l + 1, r, cur + "(")
            dfs(l, r + 1, cur + ")")

        res = []
        dfs(0, 0, "")
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = "()"

        def dfs(i, cur, l, r):
            if i == n * 2:
                res.append(cur)
                return

            if l == n:
                dfs(i + 1, cur + s[1], l, r + 1)
            elif i == 0 or l == r:
                dfs(i + 1, cur + s[0], l + 1, r)
            else:
                dfs(i + 1, cur + s[0], l + 1, r)
                dfs(i + 1, cur + s[1], l, r + 1)

        dfs(0, "", 0, 0)
        return res
