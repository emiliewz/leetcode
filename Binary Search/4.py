# 4. Median of Two Sorted Arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        odd = (m + n) % 2
        mid = (m + n + 1) // 2
        l, h = 0, m
        while l <= h:
            m1 = l + (h - l) // 2
            m2 = mid - m1
            l1 = nums1[m1 - 1] if m1 - 1 >= 0 else float("-inf")
            h1 = nums1[m1] if m1 < m else float("inf")
            l2 = nums2[m2 - 1] if m2 - 1 >= 0 else float("-inf")
            h2 = nums2[m2] if m2 < n else float("inf")

            if l1 <= h2 and l2 <= h1:
                if odd:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(h1, h2)) / 2
            elif l1 > h2:
                h = m1 - 1
            else:
                l = m1 + 1

        return -1
