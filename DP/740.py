# 740. Delete and Earn
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = max(nums) + 1
        freq = [0] * n
        for i in nums:
            freq[i] += i

        max_points = [0] * n
        max_points[1] = freq[1]

        for i in range(2, n):
            max_points[i] = max(max_points[i - 2] + freq[i], max_points[i - 1])

        return max_points[-1]


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = max(nums) + 1
        freq = [0] * n
        for i in nums:
            freq[i] += i

        dp = [0] * (n + 1)
        dp[-2] = freq[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 2] + freq[i], dp[i + 1])
        return dp[0]
