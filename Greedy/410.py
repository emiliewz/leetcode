# 410. Split Array Largest Sum
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(tar):
            cur, count = 0, 0
            for i in nums:
                if cur + i > tar:
                    cur = i
                    count += 1
                else:
                    cur += i
            return count < k

        l, h = max(nums), sum(nums)
        while l <= h:
            mid = l + (h - l) // 2
            if canSplit(mid):
                h = mid - 1
            else:
                l = mid + 1

        return l
