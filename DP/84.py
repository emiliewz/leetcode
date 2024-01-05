# 84. Largest Rectangle in Histogram
from typing import List


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
