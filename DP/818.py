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


class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 1))
        res = 0

        while q:
            for _ in range(len(q)):
                p, s = q.popleft()
                if p == target:
                    return res

                q.append((p + s, s * 2))
                if (p + s > target and s > 0) or (p + s < target and s < 0):
                    q.append((p, -1 if s > 0 else 1))

            res += 1

        return -1


class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        q = deque()
        q.append([0, 1, 0])

        while q:
            p, s, i = q.popleft()
            if p == target:
                return i
            q.append([p + s, s * 2, i + 1])
            if (p + s > target and s > 0) or (p + s < target and s < 0):
                q.append([p, -1 if s > 0 else 1, i + 1])

        return -1
