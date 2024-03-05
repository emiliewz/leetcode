# 1016. Binary String With Substrings Representing 1 To N
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n, 0, -1):
            cur = bin(i)[2:]
            if cur not in s:
                return False
        return True
