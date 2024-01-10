# 1024. Video Stitching
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [float("inf")] * 101
        dp[0] = 0

        for s, e in clips:
            for i in range(s, e + 1):
                dp[i] = min(dp[s] + 1, dp[i])

        return dp[time] if dp[time] != float("inf") else -1
