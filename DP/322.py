# 322. Coin Change
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        dp = [float("inf")] * (amount + 1)

        for i in range(amount + 1):
            for j in coins:
                if i == j:
                    dp[i] = 1
                if i > j:
                    dp[i] = min(dp[j] + dp[i - j], dp[i])

        return dp[-1] if dp[-1] != float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        dp = [float("inf")] * (amount + 1)

        for i in range(amount + 1):
            for j in range(i):
                if i in coins:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[j] + dp[i - j], dp[i])

        return dp[-1] if dp[-1] != float("inf") else -1
