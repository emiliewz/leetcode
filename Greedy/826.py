# 826. Most Profit Assigning Work
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        n = len(difficulty)
        res = j = cur = 0
        worker.sort()
        for i in worker:
            while j < n and i >= jobs[j][0]:
                if jobs[j][1] > cur:
                    cur = jobs[j][1]
                j += 1
            res += cur

        return res
