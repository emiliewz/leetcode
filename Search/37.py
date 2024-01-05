# 37. Sudoku Solver
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, blocks = (
            [[0] * 10 for _ in range(9)],
            [[0] * 10 for _ in range(9)],
            [[0] * 10 for _ in range(9)],
        )
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != ".":
                    rows[i][int(n)] = 1
                    cols[j][int(n)] = 1
                    blocks[(j // 3) * 3 + i // 3][int(n)] = 1

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)
            for i in range(1, 10):
                if (
                    not rows[r][i]
                    and not cols[c][i]
                    and not blocks[(c // 3) * 3 + r // 3][i]
                ):
                    board[r][c] = str(i)
                    rows[r][i] = 1
                    cols[c][i] = 1
                    blocks[(c // 3) * 3 + r // 3][i] = 1
                    if backtrack(r, c + 1):
                        return True
                    board[r][c] = "."
                    rows[r][i] = 0
                    cols[c][i] = 0
                    blocks[(c // 3) * 3 + r // 3][i] = 0

        backtrack(0, 0)
