# 321. Create Maximum Number
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def prep(nums, i):
            k = len(nums) - i
            res = []
            for num in nums:
                while k and res and res[-1] < num:
                    res.pop()
                    k -= 1
                res.append(num)
            return res[:i]

        def merge(a, b):
            m, n = len(a), len(b)
            res = []
            while a and b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            if a:
                res += a
            if b:
                res += b
            return res

        return max(
            merge(prep(nums1, i), prep(nums2, k - i))
            for i in range(k + 1)
            if i <= len(nums1) and k - i <= len(nums2)
        )
