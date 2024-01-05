# 52. N-Queens II
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
