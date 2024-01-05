# 46. Permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, cur):
            if not nums:
                res.append(cur[::])
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :], cur + [nums[i]])

        dfs(nums, [])
        return res
