# 410. Split Array Largest Sum
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(tar):
            cur, count = 0, 1
            for n in nums:
                cur += n
                if cur > tar:
                    cur = n
                    count += 1
            return count <= k

        l, h = max(nums), sum(nums)

        while l <= h:
            mid = l + (h - l) // 2
            if canSplit(mid):
                h = mid - 1
            else:
                l = mid + 1

        return l
