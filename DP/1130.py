# 1130. Minimum Cost Tree From Leaf Values
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1 : i] + arr[i + 1 : i + 2]) * arr.pop(i)

        return res
