# 39. Combination Sum
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, cur, total):
            if i == n:
                return
            if total == target:
                res.append(cur)
                return

            if total + candidates[i] <= target:
                dfs(i, cur + [candidates[i]], total + candidates[i])
                dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res
