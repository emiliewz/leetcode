# 40. Combination Sum II
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(pos, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                # backtrack(i+1, cur+[candidates[i]], total+candidates[i])
                backtrack(i + 1, cur, total + candidates[i])
                cur.pop()

        backtrack(0, [], 0)
        return res
