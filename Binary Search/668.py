# 668. Kth Smallest Number in Multiplication Table
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, h = 1, m * n

        while l < h:
            mid = l + ((h - l) >> 1)
            count = 0
            j = n - 1
            for i in range(1, m + 1):
                count += n if n <= mid // i else mid // i
            if count < k:
                l = mid + 1
            else:
                h = mid

        return l
