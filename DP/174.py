# 174. Dungeon Game
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        a = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        a[m - 1][n] = a[m][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                a[i][j] = max(min(a[i + 1][j], a[i][j + 1]) - dungeon[i][j], 1)

        return a[0][0]


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        min_hp = [[2000] * (n + 1) for _ in range(m + 1)]
        min_hp[m - 1][n] = min_hp[m][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_hp[i][j] = max(
                    min(min_hp[i + 1][j], min_hp[i][j + 1]) - dungeon[i][j], 1
                )

        return min_hp[0][0]
