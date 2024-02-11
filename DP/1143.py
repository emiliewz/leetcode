# 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        a = [0] * (n + 1)

        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    a[j] = tmp[j - 1] + 1
                else:
                    a[j] = max(tmp[j], a[j - 1])

        return a[-1]
