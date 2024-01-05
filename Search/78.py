# 78. Subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(pos, cur):
            res.append(cur)
            if len(cur) == len(nums):
                return

            for i in range(pos, len(nums)):
                dfs(i + 1, cur + [nums[i]])

        dfs(0, [])
        return res
