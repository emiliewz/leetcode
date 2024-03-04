# 677. Map Sum Pairs
class MapSum:

    def __init__(self):
        self.a = {}

    def insert(self, key: str, val: int) -> None:
        self.a[key] = val

    def sum(self, prefix: str) -> int:
        return sum(j for i, j in self.a.items() if i.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
