# 1335. Minimum Difficulty of a Job Schedule
from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        @cache
        def dp(i, k):
            if k == 1:
                return max(jobDifficulty[i:])

            min_difficulty = float("inf")

            for j in range(i, n - k + 1):
                min_difficulty = min(
                    max(jobDifficulty[i : j + 1]) + dp(j + 1, k - 1), min_difficulty
                )

            return min_difficulty

        return dp(0, d)
