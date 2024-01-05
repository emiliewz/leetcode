# 77. Combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(pos, cur):
            if len(cur) == k:
                res.append(cur)
                return

            for i in range(pos, n + 1):
                dfs(i + 1, cur + [i])

        dfs(1, [])
        return res
