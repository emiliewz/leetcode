# 752. Open the Lock
from typing import Deque, List


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

        q = Deque()
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
