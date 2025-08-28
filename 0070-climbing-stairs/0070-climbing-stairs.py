class Solution:
    def climbStairs(self, n: int) -> int:
        f = 1
        s = 1

        for _ in range(n-1):
            f, s = f+s, f

        return f
