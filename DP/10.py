# 10. Regular Expression Matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        a = [False] * (n + 1)
        a[0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                a[j] = a[j - 2]

        for i in range(1, m + 1):
            tmp = a[:]
            a = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    a[j] = a[j - 2] or (tmp[j] and p[j - 2] in [".", s[i - 1]])
                elif p[j - 1] in [s[i - 1], "."]:
                    a[j] = tmp[j - 1]

        return a[-1]
