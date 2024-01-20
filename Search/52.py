# 52. N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        def dfs(queens, summ, diff):
            nonlocal res
            row = len(queens)
            if row == n:
                res += 1
                return

            for col in range(n):
                if col in queens or row + col in summ or row - col in diff:
                    continue
                dfs(queens + [col], summ + [row + col], diff + [row - col])

        dfs([], [], [])
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        queens, summ, diff = set(), set(), set()

        def dfs(row):
            nonlocal res
            if row == n:
                res += 1
                return

            for col in range(n):
                if col in queens or row + col in summ or row - col in diff:
                    continue
                summ.add(row + col)
                diff.add(row - col)
                queens.add(col)
                dfs(row + 1)
                summ.remove(row + col)
                diff.remove(row - col)
                queens.remove(col)

        dfs(0)
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        summ, diff = set(), set()

        def dfs(queens):
            nonlocal res
            row = len(queens)
            if row == n:
                res += 1
                return

            for col in range(n):
                if col in queens or row + col in summ or row - col in diff:
                    continue
                summ.add(row + col)
                diff.add(row - col)
                dfs(queens + [col])
                summ.remove(row + col)
                diff.remove(row - col)

        dfs([])
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        negDiag = set()
        posDiag = set()
        col = set()

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return

            for i in range(n):
                if i in col or r - i in negDiag or r + i in posDiag:
                    continue
                negDiag.add(r - i)
                posDiag.add(r + i)
                col.add(i)
                backtrack(r + 1)
                negDiag.remove(r - i)
                posDiag.remove(r + i)
                col.remove(i)

        backtrack(0)
        return res
