# 718. Maximum Length of Repeated Subarray
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        a, res = [0] * (n + 1), 0

        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                a[j] = tmp[j - 1] + 1 if nums1[i - 1] == nums2[j - 1] else 0
            res = max(res, max(a))

        return res
