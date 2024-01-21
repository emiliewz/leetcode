# 542. 01 Matrix
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        a = mat[:]

        for i in range(m):
            for j in range(n):
                if a[i][j]:
                    top = a[i - 1][j] if i > 0 else m + n
                    left = a[i][j - 1] if j > 0 else m + n
                    a[i][j] = min(top, left) + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if a[i][j]:
                    bottom = a[i + 1][j] if i + 1 < m else m + n
                    right = a[i][j + 1] if j + 1 < n else m + n
                    a[i][j] = min(a[i][j], min(bottom, right) + 1)

        return a


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        ans = [[r + c] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    top = ans[i - 1][j] if i > 0 else r + c
                    left = ans[i][j - 1] if j > 0 else r + c
                    ans[i][j] = min(top, left) + 1

        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    down = ans[i + 1][j] if i < r - 1 else r + c
                    right = ans[i][j + 1] if j < c - 1 else r + c
                    ans[i][j] = min(ans[i][j], min(down, right) + 1)

        return ans


# BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])

        q = deque()
        visit = set()
        ans = [[0] * c for _ in range(r)]
        directions = [0, 1, 0, -1, 0]

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if mat[x][y] == 1:
                    ans[x][y] = dist

                for i in range(0, 4):
                    nx = x + directions[i]
                    ny = y + directions[i + 1]
                    if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visit:
                        q.append((nx, ny))
                        visit.add((nx, ny))
            dist += 1
        return ans


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        q = deque()
        m = len(mat)
        n = len(mat[0])
        MAX_VALUE = m * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    q.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat
