# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        a = [i for i in range(n + 1)]

        for i in range(1, m + 1):
            tmp = a[:]
            a[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    a[j] = tmp[j - 1]
                else:

                    a[j] = min(tmp[j], tmp[j - 1], a[j - 1]) + 1

        return a[-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        a = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            a[i][0] = i

        for j in range(n + 1):
            a[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    a[i][j] = a[i - 1][j - 1]
                else:
                    a[i][j] = min(a[i - 1][j], a[i][j - 1], a[i - 1][j - 1]) + 1
        return a[-1][-1]


class Solution:
    def minDistance(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        a = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            a[i][0] = i

        for j in range(n + 1):
            a[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    a[i][j] = a[i - 1][j - 1]
                else:
                    # delete, insect, replace backwords
                    # a[i][j] = min(a[i+1][j], a[i][j+1], a[i+1][j+1])+1
                    # delete, insect, replace forwards
                    a[i][j] = min(a[i - 1][j], a[i][j - 1], a[i - 1][j - 1]) + 1

        return a[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]
