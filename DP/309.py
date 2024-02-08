# 309. Best Time to Buy and Sell Stock with Cooldown
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        cool_down = 0
        hold = -float("inf")

        for p in prices:
            hold, sell, cool_down = (
                max(cool_down - p, hold),
                hold + p,
                max(sell, cool_down),
            )

        return max(sell, cool_down)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -float("inf")
        hold = 0
        sell = 0

        for p in prices:
            hold, buy, sell = max(buy, hold, sell), max(hold - p, buy), buy + p

        return max(sell, hold)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rest, sold, hold = 0, 0, -float("inf")

        for i in prices:
            prev_sold = sold
            sold = hold + i
            hold = max(rest - i, hold)
            rest = max(rest, prev_sold)

        return max(sold, rest)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -float("inf")

        for i in prices:
            prev_sell = sell
            sell = hold + i
            hold = max(hold, cool_down - i)
            cool_down = max(cool_down, prev_sell)

        return max(sell, cool_down)
