# 309. Best Time to Buy and Sell Stock with Cooldown
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -float("inf")

        for i in prices:
            prev_sell = sell
            sell = hold + i
            hold = max(hold, cool_down - i)
            cool_down = max(cool_down, prev_sell)

        return max(sell, cool_down)
