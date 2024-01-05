# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                steps[i][j] = steps[i - 1][j] + steps[i][j - 1]

        return steps[-1][-1]
