# 1187. Make Array Strictly Increasing
from bisect import bisect_left, bisect_right
from functools import cache
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m, n = len(arr1), len(arr2)
        arr2.sort()
        memo = {}

        def dp(i, prev_max):
            if i == m:
                return 0
            if (i, prev_max) in memo:
                return memo[(i, prev_max)]
            j = bisect_right(arr2, prev_max)
            ans = float("inf")
            if arr1[i] > prev_max:
                ans = min(dp(i + 1, arr1[i]), ans)
            if j < n:
                ans = min(dp(i + 1, arr2[j]) + 1, ans)
            memo[(i, prev_max)] = ans
            return ans

        res = dp(0, -1)
        return res if res != float("inf") else -1


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m, n = len(arr1), len(arr2)
        arr2.sort()

        @cache
        def dp(i, prev_max):
            if i == m:
                return 0
            j = bisect_right(arr2, prev_max)
            ans = float("inf")
            if arr1[i] > prev_max:
                ans = min(ans, dp(i + 1, arr1[i]))
            if j < n:
                ans = min(ans, dp(i + 1, arr2[j]) + 1)
            return ans

        res = dp(0, -1)
        return res if res <= m else -1


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        nums = sorted(set(arr2))
        m, n = len(arr1), len(nums)

        @cache
        def dp(i, prev_max):
            if i == m:
                return 0

            # j = bisect_left(nums, prev_max+1)
            j = bisect_right(nums, prev_max)

            return min(
                dp(i + 1, nums[j]) + 1 if j < n else float("inf"),
                dp(i + 1, arr1[i]) if (i == 0 or arr1[i] > prev_max) else float("inf"),
            )

        res = dp(0, -1)
        return res if res != float("inf") else -1
