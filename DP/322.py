# 322. Coin Change
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [float("inf")] * (amount + 1)
        coins.sort()
        a[0] = 0

        for coin in coins:
            if coin > amount:
                break
            for i in range(coin, amount + 1):
                a[i] = min(a[i], a[i - coin] + 1)

        return a[amount] if a[amount] != float("inf") else -1
