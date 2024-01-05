# 85. Maximal Rectangle
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        height = [0] * (n + 1)
        res = 0

        def max_area(height):
            res = 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    left_most = stack.pop()
                    prev_smaller = stack[-1]
                    h = height[left_most]
                    w = i - prev_smaller - 1
                    res = max(res, h * w)
                stack.append(i)
            return res

        for i in range(m):
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == "1" else 0
            res = max(res, max_area(height))

        return res
