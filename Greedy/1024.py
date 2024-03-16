# 1024. Video Stitching
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda c: (c[0], -c[1]))
        if clips[0][0] > 0:
            return -1
        a = [float("inf")] * 101
        a[0] = 0

        for clip in clips:
            start, end = clip
            if a[start] == float("inf"):
                return a[time] if a[time] != float("inf") else -1
            for i in range(start + 1, end + 1):
                a[i] = min(a[i], a[start] + 1)

        return a[time] if a[time] != float("inf") else -1


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        a = [0] * 101
        for l, r in clips:
            a[l] = max(a[l], r)

        res = 0
        l = r = 0
        while r < time:
            l, r = r, max(a[l : r + 1])
            if r <= l:
                return -1
            res += 1
        return res
