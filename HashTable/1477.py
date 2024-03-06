# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        a = {0: -1}
        total, res = 0, float("inf")
        candidates = [(-1, float("inf"))]
        for i, n in enumerate(arr):
            total += n
            if total - target in a:
                j = a[total - target]
                cur = i - j
                for ends, prev in candidates[::-1]:
                    if ends <= j:
                        if cur + prev < res:
                            res = prev + cur
                        break
                if cur < candidates[-1][-1]:
                    candidates.append((i, cur))
            a[total] = i
        return res if res != float("inf") else -1
