# 717. 1-bit and 2-bit Characters
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if n == 1 or bits[-2] == 0:
            return True

        i = 0
        while i < n:
            if bits[i] == 0:
                if i == n - 1:
                    return True
                i += 1
            else:
                i += 2

        return False
