# 85. Maximal Rectangle
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_max_area(heights):
            stack = [-1]
            max_area = 0

            for i in range(n + 1):
                while heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    max_area = max(max_area, w * h)
                stack.append(i)
            return max_area

        m, n = len(matrix), len(matrix[0])
        heights, max_area = [0] * (n + 1), 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            res = max(res, get_max_area(heights))

        return max_area
