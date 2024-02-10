# 1105. Filling Bookcase Shelves
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        a = [0] * n
        a[0] = books[0][1]

        for i in range(1, n):
            w, h = books[i]
            a[i] = a[i - 1] + h
            j = i - 1

            while w + books[j][0] < shelfWidth and j >= 0:
                w += books[j][0]
                h = max(h, books[j][1])
                a[i] = min(a[i], a[j - 1] + h if j > 0 else h)
                j -= 1

        return a[-1]
