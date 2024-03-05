# 1296. Divide Array in Sets of K Consecutive Numbers
from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for i in sorted(count):
            if count[i] > 0:
                cur = count[i]
                for j in range(i, i + k):
                    if count[j] < cur:
                        return False
                    count[j] -= cur

        return True
