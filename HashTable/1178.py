# 1178. Number of Valid Words for Each Puzzle
from collections import defaultdict
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def getmask(word):
            mask = 0
            for c in word:
                i = ord(c) - ord("a")
                mask |= 1 << i
            return mask

        a, res = defaultdict(int), [0] * len(puzzles)
        for i, w in enumerate(words):
            wordInBits = getmask(w)
            a[wordInBits] += 1

        for i, p in enumerate(puzzles):
            mask = getmask(p[1:])
            total = 0
            firstLetter = 1 << (ord(p[0]) - ord("a"))
            curmask = mask
            while curmask:
                total += a[curmask | firstLetter]
                curmask = (curmask - 1) & mask
            total += a[firstLetter]
            res[i] = total
        return res
