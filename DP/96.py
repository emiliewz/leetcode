# 96. Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        if n < 3:
            return n
        a = [0] * (n + 1)
        a[1] = a[0] = 1
        for i in range(2, n + 1):
            for j in range(i):
                a[i] += a[i - j - 1] * a[j]
        return a[n]


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]
