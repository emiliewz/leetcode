# 51. N-Queens
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        col = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for i in range(n):
                if i not in col and r + i not in posDiag and r - i not in negDiag:
                    board[r][i] = "Q"
                    negDiag.add(r - i)
                    posDiag.add(r + i)
                    col.add(i)

                    backtrack(r + 1)

                    board[r][i] = "."
                    negDiag.remove(r - i)
                    posDiag.remove(r + i)
                    col.remove(i)

        backtrack(0)
        return res
