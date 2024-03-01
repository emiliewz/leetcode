# 381. Insert Delete GetRandom O(1) - Duplicates allowed
from collections import defaultdict
from random import randint


class RandomizedCollection:

    def __init__(self):
        self.a = defaultdict(set)
        self.size = 0
        self.data = []

    def insert(self, val: int) -> bool:
        res = val not in self.a
        self.data.append(val)
        self.a[val].add(self.size)
        self.size += 1
        return res

    def remove(self, val: int) -> bool:
        if val in self.a:
            last = self.data[-1]
            self.data.pop()
            self.size -= 1

            if last == val:
                self.a[val].remove(self.size)
                if not self.a[val]:
                    del self.a[val]
                return True

            i = self.a[val].pop()
            if not self.a[val]:
                del self.a[val]

            self.data[i] = last
            self.a[last].remove(self.size)
            self.a[last].add(i)
            return True
        return False

    def getRandom(self) -> int:
        i = randint(0, self.size - 1)
        return self.data[i]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
