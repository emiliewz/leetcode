# 733. Flood Fill
from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        cur = image[sr][sc]
        if cur == color:
            return image

        q = deque()
        q.append((sr, sc))

        while q:
            cx, cy = q.popleft()
            image[cx][cy] = color

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == cur:
                    q.append((nx, ny))

        return image
