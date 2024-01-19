# 1024. Video Stitching
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0:
            return 0

        clips.sort()
        if clips[0][0] > 0:
            return -1

        a = [float("inf")] * (time + 1)
        a[0] = 0

        for s, e in clips:
            for i in range(s, min(e, time) + 1):
                if s <= i <= e:
                    a[i] = min(a[s] + 1, a[i])

        return a[-1] if a[-1] != float("inf") else -1


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0:
            return 0

        clips.sort()
        if clips[0][0] > 0:
            return -1

        a = [float("inf")] * (time + 1)
        a[0] = 0

        for i in range(1, time + 1):
            for s, e in clips:
                if s <= i <= e:
                    a[i] = min(a[s] + 1, a[i])

        return a[-1] if a[-1] != float("inf") else -1


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0:
            return 0
        n = len(clips)
        clips.sort(key=lambda x: (x[0], -x[1]))
        if clips[0][0] > 0:
            return -1

        i = 1
        stack = [clips[0]]
        while stack[-1][1] < time and i < n:
            s, e = clips[i]
            if s <= stack[-1][1] < e:
                if len(stack) > 1 and s <= stack[-2][1]:
                    stack.pop()
                stack.append(clips[i])
            i += 1

        if stack[-1][1] >= time:
            return len(stack)
        return -1


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [float("inf")] * 101
        dp[0] = 0

        for s, e in clips:
            for i in range(s, e + 1):
                dp[i] = min(dp[s] + 1, dp[i])

        return dp[time] if dp[time] != float("inf") else -1
