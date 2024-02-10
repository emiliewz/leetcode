# 309. Best Time to Buy and Sell Stock with Cooldown
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, rest, hold = 0, 0, -float("inf")

        for p in prices:
            hold, sell, rest = (
                hold + p,
                max(rest - p, hold),
                max(sell, rest),
            )

        return max(sell, rest)
