# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for p in prices:
            if p < buy:
                buy = p
            max_profit = max(max_profit, p - buy)

        return max_profit
