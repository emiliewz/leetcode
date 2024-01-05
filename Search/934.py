# 934. Shortest Bridge
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()

        direct = [0, 1, 0, -1, 0]

        def inValid(x, y):
            return x < 0 or y < 0 or x >= N or y >= N

        def dfs(x, y):
            if inValid(x, y) or grid[x][y] == 0 or (x, y) in visit:
                return
            visit.add((x, y))
            for i in range(4):
                dfs(x + direct[i], y + direct[i + 1])

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for j in range(4):
                        curR = r + direct[j]
                        curC = c + direct[j + 1]
                        if inValid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        visit.add((curR, curC))
                        q.append((curR, curC))
                res += 1
            return -1
        
        i, j = next((i,j) for i in range(N) for j in range(N) if grid[i][j])
        dfs(i, j)
        return bfs()
                
        # for i in range(N):
        #     for j in range(N):
        #         if grid[i][j]:
        #             dfs(i, j)
        #             return bfs()
