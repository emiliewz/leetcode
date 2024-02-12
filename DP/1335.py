# 1335. Minimum Difficulty of a Job Schedule
from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + jobDifficulty[i - 1]

        @cache
        def dfs(i, d):
            if d == n - i:
                return sums[n] - sums[i]

            if d == 1:
                return max(jobDifficulty[i:])

            res = float("inf")
            cur_max = 0
            for j in range(i + 1, n):
                cur_max = max(cur_max, jobDifficulty[j - 1])
                res = min(res, cur_max + dfs(j, d - 1))

            return res

        return dfs(0, d)
