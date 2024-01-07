# 89. Gray Code
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res += [res[j] | (1 << i)]

        return res


class Solution:
    def grayCode(self, n: int) -> List[int]:
        nums = 1 << n
        gray_codes = [i ^ (i >> 1) for i in range(nums)]
        return gray_codes


class Solution:
    def grayCode(self, n: int) -> List[int]:
        nums = 1 << n
        gray_codes = [i ^ (i // 2) for i in range(nums)]
        return gray_codes
