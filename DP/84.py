# 84. Largest Rectangle in Histogram
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights += [0]
        n = len(heights)
        max_area = 0

        for i in range(n):
            while heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                w = i - 1 - stack[-1]
                h = heights[cur]
                max_area = max(max_area, w * h)
            stack.append(i)

        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        max_ra = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_ra = max(max_ra, h * w)
            stack.append(i)
        heights.pop()
        return max_ra


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        max_area = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                left_most = stack.pop()
                h = heights[left_most]
                w = i - 1 - stack[-1]
                max_area = max(h * w, max_area)
            stack.append(i)

        return max_area
