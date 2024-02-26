# 167. Two Sum II - Input Array Is Sorted
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {}
        n = len(numbers)
        for i, j in enumerate(numbers):
            if target - j in a:
                return [a[target - j], i + 1]
            a[j] = i + 1
