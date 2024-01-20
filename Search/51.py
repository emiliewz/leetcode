# 51. N-Queens
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        summ = set()
        diff = set()

        def dfs(q):
            row = len(q)
            if row == n:
                res.append(q)
                return
            for col in range(n):
                if col in q or row + col in summ or row - col in diff:
                    continue
                diff.add(row - col)
                summ.add(row + col)
                dfs(q + [col])
                diff.remove(row - col)
                summ.remove(row + col)

        dfs([])
        return [["." * i + "Q" + "." * (n - i - 1) for i in queens] for queens in res]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, diff, summ):
            row = len(queens)
            if row == n:
                res.append(["." * i + "Q" + "." * (n - i - 1) for i in queens])
                return
            for col in range(n):
                if col in queens or row + col in summ or row - col in diff:
                    continue
                dfs(queens + [col], diff + [row - col], summ + [row + col])

        res = []
        dfs([], [], [])
        return res


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
