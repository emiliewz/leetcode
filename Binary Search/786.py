# 786. K-th Smallest Prime Fraction
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, h = 0, 1
        while l < h:
            mid = l + (h - l) / 2
            p, q = 0, 1
            count = 0
            j = 0
            for i in range(n):
                while j < n and arr[i] / arr[j] > mid:
                    j += 1
                if j < n and p / q < arr[i] / arr[j]:
                    p, q = arr[i], arr[j]
                count += n - j

            if count < k:
                l = mid
            elif count > k:
                h = mid
            else:
                return [p, q]
