# 546. Remove Boxes
from functools import cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @cache
        def dfs(i, j, k):
            if i > j:
                return 0
            cur = i + 1
            count = 1
            while cur <= j and boxes[cur] == boxes[cur - 1]:
                cur += 1
                count += 1

            res = dfs(cur, j, 0) + (k + count) ** 2

            for h in range(cur, j + 1):
                if boxes[h] == boxes[i]:
                    res = max(res, dfs(cur, h - 1, 0) + dfs(h, j, k + count))
            return res

        return dfs(0, n - 1, 0)
