# 873. Length of Longest Fibonacci Subsequence
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        A = set(arr)
        n, res = len(arr), 0
        for i in range(n):
            for j in range(i + 1, n):
                a, b, l = arr[i], arr[j], 0
                while a + b in A:
                    a, b, l = b, a + b, l + 1
                if l > res:
                    res = l
        return res + 2 if res else 0
