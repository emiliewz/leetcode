# 93. Restore IP Addresses
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def dfs(i, cur, k):
            if k > 4:
                return
            if i == n and k == 4:
                res.append(cur[:-1])
                return

            for j in range(i, min(i + 3, n)):
                if (j > i and s[i] == "0") or int(s[i : j + 1]) > 255:
                    return
                dfs(j + 1, cur + s[i : j + 1] + ".", k + 1)

        dfs(0, "", 0)
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, k, cur):
            if i == len(s) and k == 4:
                res.append(cur[:-1])
                return
            if k >= 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i : j + 1]) < 256 and (i == j or int(s[i])):
                    backtrack(j + 1, k + 1, cur + s[i : j + 1] + ".")

        backtrack(0, 0, "")
        return res
