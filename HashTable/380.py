# 380. Insert Delete GetRandom O(1)
from random import choice


class RandomizedSet:

    def __init__(self):
        self.a = {}
        self.data = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.a:
            return False
        self.a[val] = self.size
        self.data.append(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.a:
            last = self.data[self.size - 1]
            i = self.a[val]

            self.data[i] = last
            self.a[last] = i

            self.size -= 1

            self.a.pop(val)
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
