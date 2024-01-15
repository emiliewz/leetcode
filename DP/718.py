# 718. Maximum Length of Repeated Subarray
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        a = [0] * (n + 1)
        max_v = 0
        for i in range(1, m + 1):
            tmp = a[:]
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    a[j] = 1 + tmp[j - 1]
                else:
                    a[j] = 0
            max_v = max(max_v, max(a))
        return max_v


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
            res = max(res, max(dp[i]))
        return res
