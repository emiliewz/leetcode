# 790. Domino and Tromino Tiling


class Solution:
    def numTilings(self, n: int) -> int:
        part, full, empty = 0, 1, 1

        for _ in range(n - 1):
            part, full, empty = empty + part, part * 2 + empty + full, full

        return full % (10**9 + 7)
