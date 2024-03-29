# 279. Perfect Squares
from math import isqrt, sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        a = [i for i in range(n + 1)]
        squares = [i**2 for i in range(isqrt(n) + 1)]

        for i in range(1, n + 1):
            for j in squares:
                if j > i:
                    break
                a[i] = min(a[i], a[i - j] + 1)
        return a[n]


class Solution:
    def numSquares(self, n):
        sqr = sqrt(n)
        pool = {i**2 for i in range(int(sqr) + 1)}
        test = [i**2 for i in range(int(sqr * 0.71) + 1)]

        for i in test:
            for j in test:
                if n - i - j in pool:
                    return 3 - (i == 0) - (j == 0)
        return 4
