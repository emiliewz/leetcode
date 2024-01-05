# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n <= 2:
            return 1
        f, s, t = 1, 1, 0
        for _ in range(n - 2):
            tmp = f
            f = f + s + t
            t = s
            s = tmp
        return f
