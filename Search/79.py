# 79. Word Search
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        l = len(word)

        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            if k == l - 1:
                return True

            board[i][j] = 0
            res = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )
            board[i][j] = word[k]
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])

        def dfs(x, y, i):
            if x < 0 or y < 0 or x == r or y == c or board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            cur = board[x][y]
            board[x][y] = 0
            res = (
                dfs(x + 1, y, i + 1)
                or dfs(x - 1, y, i + 1)
                or dfs(x, y + 1, i + 1)
                or dfs(x, y - 1, i + 1)
            )
            board[x][y] = cur
            return res

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True

        return False
