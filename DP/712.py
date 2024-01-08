# 712. Minimum ASCII Delete Sum for Two Strings
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        longest_common = [[0] * (n + 1) for _ in range(m + 1)]

        total = sum(ord(i) for i in s1 + s2)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    longest_common[i][j] = longest_common[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    longest_common[i][j] = max(
                        longest_common[i][j - 1], longest_common[i - 1][j]
                    )

        return total - 2 * longest_common[-1][-1]
