# 583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        longest_common = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    longest_common[i][j] = longest_common[i - 1][j - 1] + 1
                else:
                    longest_common[i][j] = max(
                        longest_common[i - 1][j], longest_common[i][j - 1]
                    )
        return m + n - 2 * longest_common[-1][-1]
