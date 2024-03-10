# 1673. Find the Most Competitive Subsequence
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        l = len(nums)
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and l - i > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack
