# 1218. Longest Arithmetic Subsequence of Given Difference
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        if n < 2:
            return 1
        a = {}

        for num in arr:
            if num - difference not in a:
                a[num] = 1
            else:
                a[num] = a[num - difference] + 1

        return max(a.values())


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}

        for n in arr:
            dp[n] = 1 + dp.get(n - difference, 0)

        return max(dp.values())


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}

        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i - difference] + 1
            else:
                dp[i] = 1
        return max(dp.values())
