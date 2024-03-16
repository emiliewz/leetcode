# 1775. Equal Sum Arrays With Minimum Number of Operations
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 > 6 * n2 or n2 > 6 * n1:
            return -1

        t1, t2 = sum(nums1), sum(nums2)
        diff = t1 - t2
        if diff < 0:
            return self.minOperations(nums2, nums1)

        nums1.sort(reverse=True)
        nums2.sort()

        res = 0
        i1, i2 = 0, 0
        while diff > 0:
            k1 = nums1[i1] - 1 if i1 < n1 else 0
            k2 = 6 - nums2[i2] if i2 < n2 else 0
            if k1 >= diff or k2 >= diff:
                return res + 1

            if k1 > k2:
                res += 1
                i1 += 1
                diff -= k1
            elif k2 > k1:
                res += 1
                i2 += 1
                diff -= k2
            else:
                res += 2
                i1 += 1
                i2 += 1
                diff -= k1 + k2

        return res
