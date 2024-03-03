# 525. Contiguous Array
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur = 0
        max_len = 0
        a = {0: -1}

        for i, j in enumerate(nums):
            if not j:
                cur -= 1
            else:
                cur += 1

            if cur in a:
                max_len = max(max_len, i - a[cur])
            else:
                a[cur] = i

        return max_len
