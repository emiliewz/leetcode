# 1130. Minimum Cost Tree From Leaf Values
from functools import cache
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dp(l, r):
            if l >= r:
                return 0
            res = float("inf")
            for k in range(l, r):
                cur_root = max(arr[l : k + 1]) * max(arr[k + 1 : r + 1])
                res = min(res, cur_root + dp(l, k) + dp(k + 1, r))
            return res

        return dp(0, len(arr) - 1)


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1 : i] + arr[i + 1 : i + 2]) * arr.pop(i)
        return res
