# 146. LRU Cache
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dict = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from left
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    # insert into the right
    def insert(self, node):
        pre = self.right.prev
        pre.next = self.right.prev = node
        node.prev, node.next = pre, self.right

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.remove(self.dict[key])
        self.insert(self.dict[key])
        return self.dict[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = Node(key, value)
        self.insert(self.dict[key])

        if len(self.dict) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.dict[lru.key]


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict[key] = self.dict.pop(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.size:
                self.size -= 1
            else:
                self.dict.pop(next(iter(self.dict)))
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
