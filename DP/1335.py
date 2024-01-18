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
        if n == d:
            return sums[n]

        @cache
        def dp(i, k):
            if k == 1:
                return max(jobDifficulty[i:])
            if k == n - i:
                return sums[n] - sums[i]

            difficulty = float("inf")
            cur_max = 0
            for j in range(i + 1, n - k + 2):
                cur_max = max(cur_max, jobDifficulty[j - 1])
                difficulty = min(cur_max + dp(j, k - 1), difficulty)
            return difficulty

        return dp(0, d)


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
