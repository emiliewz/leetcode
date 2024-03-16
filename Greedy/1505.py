# 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
import bisect
from collections import defaultdict, deque
from string import digits


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        a = defaultdict(deque)
        for i, c in enumerate(num):
            a[c].append(i)
        res, moved = "", []

        for _ in range(len(num)):
            for c in digits:
                if a[c]:
                    i = a[c][0]
                    steps = i - bisect.bisect(moved, i)
                    if steps <= k:
                        res += c
                        k -= steps
                        bisect.insort(moved, a[c].popleft())
                        break
        return res
