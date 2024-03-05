# 1218. Longest Arithmetic Subsequence of Given Difference
from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        a = defaultdict(int)
        for i, num in enumerate(arr):
            a[num] = a[num - difference] + 1
        return max(a.values())
