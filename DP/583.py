# 583. Delete Operation for Two Strings
from functools import cache


class Solution:
    def minDistance(self, A: str, B: str) -> int:
        m, n = len(A), len(B)

        a = [0] * (n + 1)
        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    a[j] = tmp[j - 1] + 1
                else:
                    a[j] = max(a[j - 1], tmp[j])
        return m + n - 2 * a[-1]


class Solution:
    def minDistance(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        a = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    a[i][j] = 1 + a[i - 1][j - 1]
                else:
                    a[i][j] = max(a[i][j - 1], a[i - 1][j])

        return m + n - 2 * a[-1][-1]


class Solution:
    def minDistance(self, A: str, B: str) -> int:
        m, n = len(A), len(B)

        @cache
        def dp(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i

            if A[i] == B[j]:
                return dp(i + 1, j + 1)
            else:
                return min(dp(i, j + 1), dp(i + 1, j)) + 1

        return dp(0, 0)


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
