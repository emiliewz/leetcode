# 689. Maximum Sum of 3 Non-Overlapping Subarrays
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        w1, w2, w3 = sum(nums[:k]), sum(nums[k : 2 * k]), sum(nums[2 * k : 3 * k])
        mw1, mw2, mw3 = w1, w1 + w2, w1 + w2 + w3
        mw1index, mw2index, mw3index = [0], [0, k], [0, k, 2 * k]

        for i in range(1, n - 3 * k + 1):
            w1 += nums[i + k - 1] - nums[i - 1]
            w2 += nums[i + 2 * k - 1] - nums[i + k - 1]
            w3 += nums[i + 3 * k - 1] - nums[i + 2 * k - 1]
            if w1 > mw1:
                mw1, mw1index = w1, [i]
            if mw1 + w2 > mw2:
                mw2, mw2index = mw1 + w2, mw1index + [i + k]
            if mw2 + w3 > mw3:
                mw3, mw3index = mw2 + w3, mw2index + [i + 2 * k]

        return mw3index
