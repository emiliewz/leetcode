# 546. Remove Boxes
from functools import cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @cache
        def dp(l, r, k):
            if l > r:
                return 0

            cur = r
            # first find the consecutive numbers starting at i
            count = 1
            cur -= 1
            while cur >= l and boxes[cur] == boxes[cur + 1]:
                cur -= 1
                count += 1

            # option 1 is to remove the current ith number
            res = dp(l, cur, 0) + (k + count) ** 2

            # option 2 is to find the same number starting at cur
            for i in range(l, cur + 1):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + count) + dp(i + 1, cur, 0))
            return res

        return dp(0, n - 1, 0)


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @cache
        def dp(l, r, k):
            if l > r:
                return 0

            cur = l
            # first find the consecutive numbers starting at i
            count = 1
            cur += 1
            while cur <= r and boxes[cur] == boxes[cur - 1]:
                cur += 1
                count += 1

            # option 1 is to remove the current ith number
            res = dp(cur, r, 0) + (k + count) ** 2

            # option 2 is to find the same number starting at cur
            for i in range(cur, r + 1):
                if boxes[i] == boxes[l]:
                    res = max(res, dp(cur, i - 1, 0) + dp(i, r, k + count))
            return res

        return dp(0, n - 1, 0)
