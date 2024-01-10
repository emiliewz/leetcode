# 813. Largest Sum of Averages
from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def dp(i, steps):
            if steps == k - 1:
                return sum(nums[i:]) / len(nums[i:])

            cur_max = 0
            for j in range(i + 1, len(nums)):
                cur_avg = sum(nums[i:j]) / (j - i)
                cur_max = max(cur_max, cur_avg + dp(j, steps + 1))

            return cur_max

        return dp(0, 0)


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def dfs(i, k):
            if k == 1:
                return sum(nums[i:]) / len(nums[i:])
            maxAvg = 0

            for j in range(i + 1, len(nums)):
                avg = sum(nums[i:j]) / len(nums[i:j])
                subarrayAvg = avg + dfs(j, k - 1)
                maxAvg = max(maxAvg, subarrayAvg)
            return maxAvg

        return dfs(0, k)
