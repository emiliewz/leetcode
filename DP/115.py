# 115. Distinct Subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        a = [0] * (n + 1)
        a[0] = 1

        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                a[j] = tmp[j]
                if s[i - 1] == t[j - 1]:
                    a[j] += tmp[j - 1]
        return a[-1]
