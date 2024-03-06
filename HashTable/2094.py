# 2094. Finding 3-Digit Even Numbers
from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        a = Counter(digits)
        for n in range(100, 1000, 2):
            cur = Counter(int(i) for i in str(n))
            if not n % 2 and a >= cur:
                res.append(n)
        return res
