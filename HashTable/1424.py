# 1424. Diagonal Traverse II
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        a = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                a[i + j].append(nums[i][j])
        return [j for _, i in a.items() for j in reversed(i)]
