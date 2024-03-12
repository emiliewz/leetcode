# 621. Task Scheduler
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        m = max(counts)
        max_count_repeat = counts.count(m)
        return max(len(tasks), (m - 1) * (n + 1) + max_count_repeat)
