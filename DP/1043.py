# 1043. Partition Array for Maximum Sum
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n <= k:
            return max(arr) * n
        a = [0] * (n + 1)

        for i in range(1, n + 1):
            cur_max = 0
            for j in range(1, min(i, k) + 1):
                cur_max = max(cur_max, arr[i - j])
                a[i] = max(a[i], cur_max * j + a[i - j])
        return a[-1]
