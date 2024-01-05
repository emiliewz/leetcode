# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_pro = 0

        for n in prices:
            if n < buy:
                buy = n
            max_pro = max(max_pro, n - buy)

        return max_pro
