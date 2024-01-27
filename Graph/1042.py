# 1042. Flower Planting With No Adjacent
from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        color = [0] * (n + 1)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, n + 1):
            color[i] = ({1, 2, 3, 4} - {color[j] for j in graph[i]}).pop()
        return color[1:]
