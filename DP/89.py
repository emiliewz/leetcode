# 89. Gray Code
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            for j in res[::-1]:
                res += [j | (1 << i)]

        return res
