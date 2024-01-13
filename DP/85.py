# 85. Maximal Rectangle
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_rect = 0
        heights_map = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "0":
                    heights_map[i][j] = heights_map[i - 1][j] + 1 if i > 0 else 1

        for heights in heights_map:
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_rect = max(max_rect, h * w)
                stack.append(i)

        return max_rect


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
