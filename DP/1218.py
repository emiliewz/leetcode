# 1218. Longest Arithmetic Subsequence of Given Difference
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}

        for n in arr:
            dp[n] = 1 + dp.get(n - difference, 0)

        return max(dp.values())
