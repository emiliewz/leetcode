# 673. Number of Longest Increasing Subsequence
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp, count = [1] * n, [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
        m = max(dp)

        return sum(c for l, c in zip(dp, count) if l == m)
