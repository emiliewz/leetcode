# 1049. Last Stone Weight II
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        if n == 2:
            return abs(stones[1] - stones[0])

        sums = sum(stones)
        tar = sums >> 1
        stones.sort()

        a = [False] * (tar + 1)
        a[0] = True

        for stone in stones:
            if stone > tar:
                break
            for i in range(tar, stone - 1, -1):
                a[i] = a[i] or a[i - stone]

        for i in range(tar, -1, -1):
            if a[i]:
                return sums - 2 * i
