# 90. Subsets II
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def dfs(i, cur):
            res.append(cur)

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                dfs(j + 1, cur + [nums[j]])

        dfs(0, [])
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)

        dfs(0, [])
        return res
