# 1092. Shortest Common Supersequence
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        def get_lcs():
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            lcs, i, j = "", m, n
            while i > 0 and j > 0:
                if str1[i - 1] == str2[j - 1]:
                    lcs = str1[i - 1] + lcs
                    j -= 1
                    i -= 1
                elif dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
            return lcs

        lcs = get_lcs()

        res, i, j = "", 0, 0
        for c in lcs:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

        res, i, j = "", 0, 0
        for c in dp[-1][-1]:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]
