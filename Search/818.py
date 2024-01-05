# 818. Race Car
from typing import Deque


class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        q = Deque()
        q.append([0, 1, 0])

        while q:
            p, s, i = q.popleft()
            if p == target:
                return i
            q.append([p + s, s * 2, i + 1])
            if (p + s > target and s > 0) or (p + s < target and s < 0):
                q.append([p, -1 if s > 0 else 1, i + 1])

        return -1
