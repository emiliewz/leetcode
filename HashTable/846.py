# 846. Hand of Straights
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for i in sorted(count):
            if count[i] > 0:
                cur = count[i]
                for j in range(i, i + groupSize):
                    if count[j] < cur:
                        return False
                    count[j] -= cur
        return True
