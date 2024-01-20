# 216. Combination Sum III
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if len(cur) > k or total > n:
                return
            if len(cur) == k:
                if total == n:
                    res.append(cur)
                return

            for j in range(i, 10):
                dfs(j + 1, cur + [j], total + j)

        dfs(1, [], 0)
        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            if len(cur) == k:
                if total == n:
                    res.append(cur)
                return

            for j in range(i, 10):
                if j > n:
                    return
                backtrack(j + 1, cur + [j], total + j)

        backtrack(1, [], 0)
        return res
