# 567. Permutation in String
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1, a2 = defaultdict(int), defaultdict(int)
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        for i in range(n1):
            a1[s1[i]] += 1
            a2[s2[i]] += 1

        if a1 == a2:
            return True
        for i in range(n1, n2):
            a2[s2[i]] += 1
            a2[s2[i - n1]] -= 1
            if a2[s2[i - n1]] == 0:
                a2.pop(s2[i - n1])
            if a1 == a2:
                return True

        return False
