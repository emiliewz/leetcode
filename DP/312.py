# 312. Burst Balloons
from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        a = [[0] * n for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i + 1, j):
                    a[i][j] = max(
                        a[i][j], nums[i] * nums[j] * nums[k] + a[i][k] + a[k][j]
                    )
        return a[0][n - 1]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = 0
            for k in range(i + 1, j):
                cur = nums[i] * nums[j] * nums[k]
                res = max(res, cur + dfs(i, k) + dfs(k, j))
            return res

        nums = [1] + nums + [1]
        n = len(nums)
        return dfs(0, n - 1)
