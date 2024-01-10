# 1262. Greatest Sum Divisible by Three
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]

        for i in nums:
            for j in dp[:]:
                dp[(j + i) % 3] = max(dp[(i + j) % 3], i + j)

        return dp[0]


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for i in nums:
            a, b, c = dp[0] + i, dp[1] + i, dp[2] + i
            dp[a % 3] = max(dp[a % 3], a)
            dp[b % 3] = max(dp[b % 3], b)
            dp[c % 3] = max(dp[c % 3], c)
        return dp[0]


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        sums = [False] * (total_sum + 1)
        sums[0] = True

        for num in nums:
            for i in range(total_sum, num - 1, -1):
                sums[i] = sums[i] or sums[i - num]

        for i in range(total_sum, -1, -1):
            if sums[i] and i % 3 == 0:
                return i
