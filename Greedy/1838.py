# 1838. Frequency of the Most Frequent Element
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, cur = -1, 0
        res = 0
        for r, n in enumerate(nums):
            cur += n
            w = r - l
            if n * w <= cur + k:
                res = max(res, w)
            else:
                l += 1
                cur -= nums[l]
        return res
