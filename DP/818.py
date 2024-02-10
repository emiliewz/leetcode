# 818. Race Car
from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        q, moves = deque([(0, 1)]), 0

        while q:
            for _ in range(len(q)):
                p, s = q.popleft()
                if p == target:
                    return moves
                q.append((p + s, s * 2))

                if (s > 0 and p + s > target) or (s < 0 and p + s < target):
                    q.append((p, 1 if s < 0 else -1))

            moves += 1

        return -1
