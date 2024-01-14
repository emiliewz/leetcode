# 1105. Filling Bookcase Shelves
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        a = [float("inf")] * n
        a[0] = books[0][1]

        for i in range(1, n):
            w, h = books[i]
            a[i] = a[i - 1] + h
            j = i - 1
            while j >= 0 and w + books[j][0] <= shelfWidth:
                w += books[j][0]
                h = max(h, books[j][1])
                a[i] = min(a[i], a[j - 1] + h if j > 0 else h)
                j -= 1
        return a[-1]


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        a = [float("inf")] * n
        a[0] = books[0][1]

        for i in range(1, n):
            w, h = books[i]
            a[i] = a[i - 1] + h

            for j in range(i - 1, -1, -1):
                prev_w, prev_h = books[j]
                w += prev_w
                if w > shelfWidth:
                    break
                h = max(h, prev_h)
                a[i] = min(a[j - 1] + h if j > 0 else h, a[i])

        return a[-1]


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float("inf")] * n
        dp[0] = books[0][1]

        for i in range(1, n):
            w, h = books[i]
            dp[i] = dp[i - 1] + h
            for j in range(i - 1, -1, -1):
                prev_w, prev_h = books[j]
                w += prev_w
                if w > shelfWidth:
                    break
                h = max(h, prev_h)
                dp[i] = min(dp[i], dp[j - 1] + h if j > 0 else h)

        return dp[n - 1]
