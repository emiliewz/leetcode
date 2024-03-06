# 2264. Largest 3-Same-Digit Number in String
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = 1
        res = ""
        for i, n in enumerate(num[1:], 1):
            if n == num[i - 1]:
                cur += 1
                if cur >= 3 and res < n:
                    res = n
            else:
                cur = 1
        return res * 3
