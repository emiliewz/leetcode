# 801. Minimum Swaps To Make Sequences Increasing
from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        keep, swap = 0, 1
        n = len(A)
        for i in range(1, n):
            cur_swap, cur_keep = n, n
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                cur_keep = keep
                cur_swap = swap + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                cur_swap = min(cur_swap, keep + 1)
                cur_keep = min(cur_keep, swap)
            keep, swap = cur_keep, cur_swap

        return min(keep, swap)


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        swap, no_swap = 1, 0
        n = len(nums1)

        for i in range(1, n):
            cur_swap, cur_no_swap = n, n
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                cur_swap = swap + 1
                cur_no_swap = no_swap
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                cur_swap = min(cur_swap, no_swap + 1)
                cur_no_swap = min(swap, cur_no_swap)
            swap = cur_swap
            no_swap = cur_no_swap

        return min(swap, no_swap)


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap = [float("inf")] * n
        no_swap = [float("inf")] * n
        swap[0] = 1
        no_swap[0] = 0

        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                swap[i] = swap[i - 1] + 1
                no_swap[i] = no_swap[i - 1]

            if nums2[i] > nums1[i - 1] and nums1[i] > nums2[i - 1]:
                swap[i] = min(swap[i], no_swap[i - 1] + 1)
                no_swap[i] = min(swap[i - 1], no_swap[i])

        return min(swap[-1], no_swap[-1])
