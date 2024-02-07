# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[0] * (n + 1) for _ in range(m + 1)]
        a[1][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a[i][j] = a[i - 1][j] + a[i][j - 1]

        return a[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                steps[i][j] = steps[i - 1][j] + steps[i][j - 1]

        return steps[-1][-1]
