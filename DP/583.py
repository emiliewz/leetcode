# 583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        a = [0] * (n + 1)

        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                a[j] = (
                    tmp[j - 1] + 1
                    if word1[i - 1] == word2[j - 1]
                    else max(tmp[j], a[j - 1])
                )

        return m + n - 2 * a[-1]
