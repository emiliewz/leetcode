# 96. Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        a = [0] * (n + 1)
        a[1] = a[0] = 1
        for i in range(2, n + 1):
            for j in range(i):
                a[i] += a[i - j - 1] * a[j]
        return a[n]
