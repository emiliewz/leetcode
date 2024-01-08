# 1143. Longest Common Subsequence
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
