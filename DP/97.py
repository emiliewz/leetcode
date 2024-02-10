# 97. Interleaving String
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        if not m or not n:
            return s1 + s2 == s3

        a = [False] * (n + 1)
        a[0] = True

        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                a[j] = a[j - 1]
            else:
                break

        for i in range(1, m + 1):
            tmp = a[:]
            a[0] = s1[i - 1] == s3[i - 1] and tmp[0]
            for j in range(1, n + 1):
                a[j] = (tmp[j] and s1[i - 1] == s3[i + j - 1]) or (
                    a[j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return a[-1]
