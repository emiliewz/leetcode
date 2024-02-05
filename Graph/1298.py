# 1298. Maximum Candies You Can Get from Boxes
from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(candies)
        initial_keys = [i for i in range(n) if status[i]]
        for b in initialBoxes:
            initial_keys += keys[b]
        have_keys = set(initial_keys)
        have_boxes = set(initialBoxes)
        q = deque(initialBoxes)
        opened = set()

        while q:
            cur = q.popleft()

            if cur in have_keys:
                opened.add(cur)
                have_keys.update(keys[cur])

                for b in containedBoxes[cur]:
                    have_boxes.add(b)
                    if b not in opened:
                        q.append(b)

        res = 0
        for i in have_keys:
            if i in have_boxes:
                res += candies[i]

        return res


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(candies)
        q = deque(initialBoxes)
        have_keys = set([i for i in range(n) if status[i]])
        have_boxes = set(initialBoxes)

        while q:
            cur = q.popleft()

            for k in keys[cur]:
                have_keys.add(k)
            for b in containedBoxes[cur]:
                have_boxes.add(b)

            if cur in have_boxes:
                for i in containedBoxes[cur]:
                    q.append(i)

        res = 0
        for k in have_keys:
            if k in have_boxes:
                res += candies[k]
        return res
