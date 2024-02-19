# 560. Subarray Sum Equals K
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, pre_sum, a = 0, 0, defaultdict(int)
        a[0] = 1

        for n in nums:
            pre_sum += n
            if pre_sum - k in a:
                res += a[pre_sum - k]
            a[pre_sum] += 1

        return res
