# 801. Minimum Swaps To Make Sequences Increasing
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep, swap = 0, 1
        n = len(nums1)
        for i in range(1, n):
            cur_swap, cur_keep = float("inf"), float("inf")
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                cur_swap = swap + 1
                cur_keep = keep
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                cur_swap = min(keep + 1, cur_swap)
                cur_keep = min(swap, cur_keep)
            swap, keep = cur_swap, cur_keep

        return min(swap, keep)
