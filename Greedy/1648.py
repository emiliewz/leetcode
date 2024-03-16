# 1648. Sell Diminishing-Valued Colored Balls
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def get(l, k):
            return (2 * l - k + 1) * k // 2 % MOD

        MOD = 10**9 + 7
        n = len(inventory)
        inventory.sort(reverse=True)
        inventory += [0]

        res, k = 0, 1
        for i in range(n):
            cur, next_num = inventory[i], inventory[i + 1]
            if cur > next_num:
                diff = cur - next_num
                if k * diff < orders:
                    res += k * (get(cur, diff))
                    orders -= k * (cur - next_num)
                else:
                    q, r = divmod(orders, k)
                    res += k * (get(cur, q)) + r * (cur - q)
                    return res % MOD
            k += 1

        return res % MOD
