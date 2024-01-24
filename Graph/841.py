# 841. Keys and Rooms
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set([0])
        n = len(rooms)
        dfs = [0]

        while dfs:
            k = dfs.pop()
            for key in rooms[k]:
                if key not in keys:
                    dfs.append(key)
                    keys.add(key)

        return len(keys) == n


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        keys = set([0])

        while dfs:
            i = dfs.pop()
            for key in rooms[i]:
                if key not in keys:
                    dfs.append(key)
                    keys.add(key)
                    if len(keys) == len(rooms):
                        return True
        return len(keys) == len(rooms)
