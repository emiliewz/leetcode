# 752. Open the Lock
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def get_neighbours(lock):
            res = []
            for i in range(4):
                res.append(lock[:i] + str((int(lock[i]) + 1 + 10) % 10) + lock[i + 1 :])
                res.append(lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i + 1 :])
            return res

        q = deque()
        q.append("0000")
        visit = set(deadends)
        visit.add("0000")
        steps = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return steps

                for c in get_neighbours(cur):
                    if c not in visit:
                        visit.add(c)
                        q.append(c)

            steps += 1

        return -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def getChildren(root):
            res = []
            for i in range(4):
                for j in range(-1, 2, 2):
                    cur = root[:i] + str((int(root[i]) + j + 10) % 10) + root[i + 1 :]
                    res.append(cur)
            return res

        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)

        while q:
            root, move = q.popleft()
            if root == target:
                return move
            for child in getChildren(root):
                if child in visit:
                    continue
                visit.add(child)
                q.append([child, move + 1])

        return -1
