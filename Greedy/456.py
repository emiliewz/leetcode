# 456. 132 Pattern
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, k = [], -float("inf")

        for n in reversed(nums):
            if n < k:
                return True
            while stack and stack[-1] < n:
                k = stack.pop()
            stack.append(n)
        return False
