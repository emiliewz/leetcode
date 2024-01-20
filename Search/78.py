# 78. Subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, cur):
            res.append(cur)
            for j in range(i, n):
                dfs(j + 1, cur + [nums[j]])

        res = []
        n = len(nums)
        dfs(0, [])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(pos, cur):
            res.append(cur)

            for i in range(pos, len(nums)):
                dfs(i + 1, cur + [nums[i]])

        dfs(0, [])
        return res
