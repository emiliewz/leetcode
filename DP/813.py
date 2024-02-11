# 813. Largest Sum of Averages
from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        @cache
        def get_sum(i, j=n):
            return sums[j] - sums[i]

        @cache
        def dfs(i, steps):
            if steps == k - 1:
                return get_sum(i) / (n - i)

            if n - i <= k - steps:
                return get_sum(i)

            res = 0
            for j in range(i + 1, n):
                cur_avg = get_sum(i, j) / (j - i)
                res = max(res, cur_avg + dfs(j, steps + 1))
            return res

        return dfs(0, 0)


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        a = [sums[i] / i for i in range(1, n + 1)]

        for j in range(2, k + 1):
            for i in range(n, j - 1, -1):
                for p in range(j - 1, i):
                    a[i - 1] = max(a[i - 1], a[p - 1] + (sums[i] - sums[p]) / (i - p))
        return a[-1]
