# 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        a = [0] * (n + 1)

        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    a[j] = tmp[j - 1] + 1
                else:
                    a[j] = max(a[j - 1], tmp[j])

        return a[-1]


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        a = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    a[i][j] = a[i - 1][j - 1] + 1
                else:
                    a[i][j] = max(a[i][j - 1], a[i - 1][j])

        return a[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        longest_common = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    longest_common[i][j] = longest_common[i - 1][j - 1] + 1
                else:
                    longest_common[i][j] = max(
                        longest_common[i - 1][j], longest_common[i][j - 1]
                    )
        return longest_common[-1][-1]
