# 981. Time Based Key-Value Store
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.a = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.a[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.a:
            return ""
        items = self.a[key]
        if items[0][0] > timestamp:
            return ""
        if items[-1][0] < timestamp:
            return items[-1][1]
        l, h = 0, len(items) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if items[mid][0] == timestamp:
                return items[mid][1]
            elif items[mid][0] < timestamp:
                l = mid + 1
            else:
                h = mid - 1

        return items[h][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
