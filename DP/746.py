# 746. Min Cost Climbing Stairs
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f, s = cost[-1], 0

        for i in range(len(cost) - 2, -1, -1):
            f, s = min(f, s) + cost[i], f

        return min(f, s)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
