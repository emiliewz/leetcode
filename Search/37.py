# 37. Sudoku Solver
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0] * 10 for _ in range(9)]
        cols = [[0] * 10 for _ in range(9)]
        boxes = [[0] * 10 for _ in range(9)]
        k = 0

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    rows[i][int(num)] = 1
                    cols[j][int(num)] = 1
                    boxes[3 * (i // 3) + j // 3][int(num)] = 1
                else:
                    k += 1

        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)
            if board[i][j] != ".":
                return dfs(i, j + 1)
            for k in range(1, 10):
                if rows[i][k] or cols[j][k] or boxes[3 * (i // 3) + j // 3][k]:
                    continue
                board[i][j] = str(k)
                rows[i][k] = 1
                cols[j][k] = 1
                boxes[3 * (i // 3) + j // 3][k] = 1
                if dfs(i, j + 1):
                    return True
                board[i][j] = "."
                rows[i][k] = 0
                cols[j][k] = 0
                boxes[3 * (i // 3) + j // 3][k] = 0

        dfs(0, 0)
        return board


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
